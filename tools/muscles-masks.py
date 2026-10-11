import sys,os,numpy as np
from PIL import Image
SP=sys.argv[1]
MAP={
 "front":{"front_delt":[4,5],"chest":[6,7],"biceps":[8,9,10,11],"forearms":[19,20,21,22],"abs":[14],"obliques":[12,13,15,16],"hip_flexors":[23,24,25],"quads":[26,27,28,29,36,37,38,39],"calves":[40,41,42,43]},
 "back":{"rear_delt":[3,4],"upper_back":[1,2,5,6,7,8],"lats":[13,14,21,22],"lower_back":[17,18],"triceps":[9,10,11,12,15,16],"forearms":[19,20,23,24,25,26,27,28,29,30,32,33],"glutes":[31],"hamstrings":[34,35,36,37,40,41,46,47,50,51],"calves":[52,53,54,55,56,57,58,59,60,61]}
}
W,H=448,600
os.makedirs("assets/muscles/m",exist_ok=True)
def save(mask,name):
    a=Image.fromarray((mask*255).astype("uint8")).resize((W,H),Image.LANCZOS)
    arr=np.asarray(a);rgba=np.zeros((H,W,4),"uint8");rgba[...,:3]=255;rgba[...,3]=arr
    Image.fromarray(rgba).save(f"assets/muscles/m/{name}.png",optimize=True)
for v,regs in MAP.items():
    lab=np.load(f"{SP}/{v}_lab.npy")
    for r,ids in regs.items():
        save(np.isin(lab,ids),f"{v}-{r}")
    # hele lichaam (incl. handen, voeten, nek) als stille basis
    im=np.asarray(Image.open(f"assets/muscles/{v}.png").convert("L")).astype(float)
    save(np.clip((190-im)/60,0,1),f"{v}-body")
print(sorted(os.listdir("assets/muscles/m")),sum(os.path.getsize("assets/muscles/m/"+f) for f in os.listdir("assets/muscles/m")))
