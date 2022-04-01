import math

def pixelateShape(sideLen,sideCount,rotation):
    if(sideCount<3):
        return
    corner=[(0,0)]
    sides=[]
    internalAngle=(180
    posX=0
    posY=0
    for i in range(1,sideCount):
        posX=posX+cos(rotation+
