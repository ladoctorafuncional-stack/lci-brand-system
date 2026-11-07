(function(){
var P=new URLSearchParams(location.search);
var W=+P.get('w')||1080,H=+P.get('h')||1350,LB=P.get('label')||'A';
var R=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true});
R.setPixelRatio(1);R.setSize(W,H);R.toneMapping=THREE.ACESFilmicToneMapping;R.toneMappingExposure=1.0;R.outputColorSpace=THREE.SRGBColorSpace;
document.body.style.margin='0';document.body.style.background='#000';document.body.appendChild(R.domElement);
var scene=new THREE.Scene();scene.fog=new THREE.Fog(0x13283a,120,520);
// backdrop gradient
(function(){var c=document.createElement('canvas');c.width=64;c.height=256;var x=c.getContext('2d');var g=x.createRadialGradient(32,110,4,32,140,200);
 g.addColorStop(0,'#5B84A3');g.addColorStop(.22,'#2E536E');g.addColorStop(.45,'#13283a');g.addColorStop(1,'#050A10');x.fillStyle=g;x.fillRect(0,0,64,256);
 var t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;scene.background=t})();
// environment (softboxes)
var pm=new THREE.PMREMGenerator(R),env=new THREE.Scene();
env.add(new THREE.Mesh(new THREE.BoxGeometry(100,100,100),new THREE.MeshBasicMaterial({color:0x04070b,side:THREE.BackSide})));
function panel(w,h,x,y,z,rx,ry,col,k){var m=new THREE.Mesh(new THREE.PlaneGeometry(w,h),new THREE.MeshBasicMaterial({color:new THREE.Color(col).multiplyScalar(k),side:THREE.DoubleSide}));m.position.set(x,y,z);m.rotation.set(rx,ry,0);env.add(m)}
panel(60,40,0,45,0,Math.PI/2,0,0xE3EBF3,6);
panel(9,80,-38,0,8,0,Math.PI/2,0x94B4CC,10);
panel(9,80,38,0,8,0,-Math.PI/2,0xE3EBF3,8);
panel(60,14,0,-8,-45,0,0,0x3E5F7A,3);
panel(30,16,0,6,46,0,Math.PI,0x94B4CC,2.2);
scene.environment=pm.fromScene(env,0.02).texture;
// materials
var glass=new THREE.MeshPhysicalMaterial({color:0xffffff,metalness:0,roughness:0.02,transmission:1,thickness:2.4,ior:1.5,envMapIntensity:1.6,attenuationColor:new THREE.Color(0xd9e8f2),attenuationDistance:60,clearcoat:1,clearcoatRoughness:0.02});
var liquid=new THREE.MeshPhysicalMaterial({color:0xcfe0ec,metalness:0,roughness:0.02,transmission:.96,thickness:18,ior:1.33,envMapIntensity:1.2,attenuationColor:new THREE.Color(0x9fc2d9),attenuationDistance:45});
var metal=new THREE.MeshStandardMaterial({color:0xc4ccd3,metalness:1,roughness:.24,envMapIntensity:1.5});
var cap=new THREE.MeshPhysicalMaterial({color:0x3E5F7A,metalness:.05,roughness:.28,clearcoat:1,clearcoatRoughness:.08,envMapIntensity:1.3});
var rubber=new THREE.MeshStandardMaterial({color:0x2b3138,roughness:.7,metalness:0});
function lathe(pts,mat,seg){var g=new THREE.LatheGeometry(pts.map(function(p){return new THREE.Vector2(p[0],p[1])}),seg||96);return new THREE.Mesh(g,mat)}
var vial=new THREE.Group();scene.add(vial);
vial.add(lathe([[0,0],[10.4,0],[11.8,1.3],[12,2.4],[12,38],[11.7,41],[10.2,45],[8.4,48.2],[7.2,50.2],[7.2,55.2],[8.5,55.7],[8.6,57.4],[0,57.4]],glass));
vial.add(lathe([[0,1.8],[10.6,1.8],[11.1,2.6],[11.1,38.2],[10.9,38.7],[0,38.7]],liquid));
var stop=lathe([[0,54.6],[6.9,54.6],[6.9,58.1],[0,58.1]],rubber);vial.add(stop);
vial.add(lathe([[0,54.8],[8.9,54.8],[8.9,56.2],[8.5,56.6],[8.5,59.2],[0,59.2]],metal));
vial.add(lathe([[0,59],[7.7,59],[8.4,59.7],[8.4,61.6],[7.5,62.3],[0,62.3]],cap));
// label
var labMesh=null,tex;
function makeLabel(img){tex=new THREE.Texture(img);tex.colorSpace=THREE.SRGBColorSpace;tex.anisotropy=R.capabilities.getMaxAnisotropy();tex.needsUpdate=true;
 var circ=2*Math.PI*12.14,lh=circ/(img.width/img.height);
 var g=new THREE.CylinderGeometry(12.14,12.14,lh,128,1,true);
 var m=new THREE.MeshPhysicalMaterial({map:tex,roughness:.42,metalness:0,clearcoat:.5,clearcoatRoughness:.2,envMapIntensity:.9,side:THREE.FrontSide});
 labMesh=new THREE.Mesh(g,m);labMesh.position.y=2.6+lh/2+3;vial.add(labMesh);}
// platform
var hexMat=new THREE.MeshBasicMaterial({color:0x94B4CC,transparent:true,opacity:.85,blending:THREE.AdditiveBlending,side:THREE.DoubleSide});
var hex1=new THREE.Mesh(new THREE.RingGeometry(34,34.8,6),hexMat);hex1.rotation.x=-Math.PI/2;hex1.rotation.z=Math.PI/6;hex1.position.y=.05;scene.add(hex1);
var hex2=new THREE.Mesh(new THREE.RingGeometry(46,46.4,6),new THREE.MeshBasicMaterial({color:0x3E5F7A,transparent:true,opacity:.7,blending:THREE.AdditiveBlending,side:THREE.DoubleSide}));hex2.rotation.x=-Math.PI/2;hex2.rotation.z=Math.PI/6;hex2.position.y=.05;scene.add(hex2);
// glow disc
(function(){var c=document.createElement('canvas');c.width=c.height=256;var x=c.getContext('2d');var g=x.createRadialGradient(128,128,0,128,128,128);g.addColorStop(0,'rgba(148,180,204,.55)');g.addColorStop(.45,'rgba(62,95,122,.22)');g.addColorStop(1,'rgba(0,0,0,0)');x.fillStyle=g;x.fillRect(0,0,256,256);
 var t=new THREE.CanvasTexture(c);var m=new THREE.Mesh(new THREE.PlaneGeometry(150,150),new THREE.MeshBasicMaterial({map:t,transparent:true,blending:THREE.AdditiveBlending,depthWrite:false}));m.rotation.x=-Math.PI/2;m.position.y=.03;scene.add(m)})();
var floor=new THREE.Mesh(new THREE.CircleGeometry(400,64),new THREE.MeshStandardMaterial({color:0x0a1118,metalness:.85,roughness:.2,envMapIntensity:.5}));floor.rotation.x=-Math.PI/2;floor.position.y=-.02;scene.add(floor);
// lights
var key=new THREE.DirectionalLight(0xE3EBF3,1.2);key.position.set(60,90,80);scene.add(key);
var rim=new THREE.DirectionalLight(0x94B4CC,2.2);rim.position.set(-80,40,-60);scene.add(rim);
var cam=new THREE.PerspectiveCamera(28,W/H,1,2000);
var shot={ry:+P.get('ry')||0,cy:+P.get('cy')||31,d:+P.get('d')||205,el:+P.get('el')||8,ty:+P.get('ty')||31};
function place(s){var el=s.el*Math.PI/180;cam.position.set(0,s.ty+Math.sin(el)*s.d,Math.cos(el)*s.d);cam.lookAt(0,s.cy,0);cam.updateProjectionMatrix()}
window.state={labelRot:P.get('lr')!==null?+P.get('lr'):-1.65,vialRy:0,vialRx:0,vialY:0,cam:shot};
window.draw=function(){vial.rotation.set(state.vialRx,state.vialRy,0);vial.position.y=state.vialY;if(labMesh)labMesh.rotation.y=state.labelRot;place(state.cam);R.render(scene,cam)};
window.THREE_SCENE={scene:scene,cam:cam,vial:vial,hex1:hex1,hex2:hex2,R:R};
var im=new Image();im.onload=function(){makeLabel(im);window.draw();window.ready=true};im.src=window.LABELS[LB];
})();
