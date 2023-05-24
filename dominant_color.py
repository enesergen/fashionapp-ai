from colorthief import ColorThief
import matplotlib.pyplot as plt
import numpy as np
import math
Black=(0,0,0)
White=(255,255,255)
Red	=(255,0,0)
Lime=(0,255,0)
Blue=(0,0,255)
Yellow=(255,255,0)
Cyan=(0,255,255)
Magenta=(255,0,255)
Silver=(192,192,192)
Gray=(128,128,128)
Maroon=(128,0,0)
Olive=(128,128,0)
Green=(0,128,0)
Purple=(128,0,128)
Teal=(0,128,128)
Navy=(0,0,128)
color_list=[Black,White,Red,Lime,Blue,Yellow
            ,Cyan,Magenta,Silver,Gray,Maroon,
            Olive,Green,Purple,Teal,Navy]
result_list=["BLACK","WHITE","RED","LIME","BLUE","YELLOW"
            ,"CYAN","MAGENTA","SILVER","GRAY","MAROON",
            "OLIVE","GREEN","PURPLE","TEAL","NAVY"]
def dominant_color(url):
    ct=ColorThief(url)
    dominant_color=ct.get_color(quality=1)
    list=[]
    for i in range(0,len(color_list)):
        res=np.asarray(tuple(np.subtract(dominant_color[0],color_list[i])))
        d=0.3*math.pow(res[0],2)+0.59*math.pow(res[1],2)+0.11*math.pow(res[2],2)
        list.append(d)
    print(result_list[list.index(min(list))])
    return result_list[list.index(min(list))]
