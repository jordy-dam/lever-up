import sys,numpy as np
from PIL import Image,ImageDraw
from scipy import ndimage as ndi
SP=sys.argv[1]  # map voor tussenbestanden
for v in ("front","back"):
    im=Image.open(f"assets/muscles/{v}.png").convert("RGB");a=np.asarray(im).astype(int)
    lum=a.mean(axis=2);body=lum<150
    lab,n=ndi.label(body)
    areas=ndi.sum(body,lab,range(1,n+1))
    keep=[i+1 for i,s in enumerate(areas) if s>600]
    out=np.zeros_like(lab);
    for k,i in enumerate(keep,1): out[lab==i]=k
    np.save(f"{SP}/{v}_lab.npy",out.astype(np.int16))
    sm=im.resize((im.width//2,im.height//2));d=ImageDraw.Draw(sm)
    for k in range(1,len(keep)+1):
        m=out==k;ys,xs=np.nonzero(m);cy,cx=ys.mean(),xs.mean()
        dist=(ys-cy)**2+(xs-cx)**2;j=dist.argmin();x,y=xs[j]//2,ys[j]//2
        d.rectangle([x-11,y-8,x+11,y+8],fill=(255,230,0));d.text((x-8,y-6),str(k),fill=(0,0,0))
    sm.save(f"{SP}/{v}_num.png");print(v,len(keep),"components")
