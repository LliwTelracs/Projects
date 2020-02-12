import re

dfa=[(0,1),(2,3),(4,5),(6,0),(1,2),(3,4),(5,6)]

arr=[]
loops=[]
for i in range(len(dfa)):
    arr.append([])
    loops.append([])
    
for i in range(len(dfa)):
    zero=dfa[i][0]
    one=dfa[i][1]
    if(i==zero):loops[i].append("0")
    else:arr[zero].append([i,"0"])
    if(i==one):loops[i].append("1")
    else:arr[one].append([i,"1"])

for i in range(1,len(dfa)):
    for j in range(len(dfa)):
        tmp=[]
        for ind in range(len(arr[j])):
            k=arr[j][ind]
            
            if(k[0]==i):
                for t in arr[i]:
                    if(t[0]==j):
                        loops[j].append(t[1]+"("+str(i)+")"+k[1])
                    else:
                        tmp.append([t[0],t[1]+"("+str(i)+")"+k[1]])
            else:
                tmp.append(k)
        
        arr[j]=tmp
    arr[i]=[]

#remove all values for which there are no listed loops
for i in range(len(dfa)):
    toRemove=re.compile("\("+str(i)+"\)",flags=re.DOTALL)
    if(len(loops[i])==0):
       for k in loops:           
           for j in range(len(k)):
               
               k[j]=re.sub(toRemove,"",k[j])
print(loops)
for i in range(1,len(dfa)):
    replaceVal="("+"|".join(["("+a+")" for a in loops[i]])+")*"
    toReplace=re.compile("\("+str(i)+"\)",flags=re.DOTALL)
    for k in loops:
        for j in range(len(k)):
            k[j]=re.sub(toReplace,replaceVal,k[j])

out="("+"|".join(["("+c+")" for c in loops[0]])+")*"   
#print(out)
    
