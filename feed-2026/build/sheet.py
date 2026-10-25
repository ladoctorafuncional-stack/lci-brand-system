import sys,glob,os
from PIL import Image
def sheet(d,out,cols=6,w=360):
    fs=sorted(glob.glob(d+'/*/*.png'))
    ims=[Image.open(f).convert('RGB') for f in fs]
    h=int(w*1350/1080); rows=(len(ims)+cols-1)//cols
    S=Image.new('RGB',(cols*w,rows*h),(20,20,20))
    for i,im in enumerate(ims): S.paste(im.resize((w,h)),((i%cols)*w,(i//cols)*h))
    S.save(out,quality=85); print(out,len(ims))
if __name__=='__main__': sheet(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 6)
