import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def pixelateShape(sideLen,sideCount,rotation=0):
    if(sideCount<3):
        return
    sides=[]
    rotation=rotation*math.pi/180
    angle=math.pi*2/sideCount
    posX=0
    posY=0
    for i in range(0,sideCount):
        side=[(round(posX),round(posY))]
        slope=(math.cos(rotation+angle*i),math.sin(rotation+angle*i))
        for l in range(2*sideLen):
            posX=posX+0.5*slope[0]
            posY=posY+0.5*slope[1]
            pt=(round(posX),round(posY))
            if pt not in side:
                side.append((round(posX),round(posY)))
        sides.append(side)
    return sides


