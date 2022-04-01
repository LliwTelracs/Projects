
nDice=30
maxVal=100
result=999

tabulation={}


def dieRollChance(dCount,dMax,val):
    if(val<=dCount):
        return 1
    if(val>dMax*dCount):
        return 0
    if(dCount==1):
        return (dMax-val+1)/dMax
    if(dCount in tabulation):
        if(val in tabulation[dCount]):
            return tabulation[dCount][val]
    else:
        tabulation[dCount]={}
    chn=0
    for i in range(1,dMax+1):
        chn=chn+dieRollChance(dCount-1,dMax,val-i)
    chn=chn/dMax
    tabulation[dCount][val]=chn
    return chn



print(dieRollChance(nDice,maxVal,result))
    
