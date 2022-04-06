
m=1
d=1
y=1980

def dayOfWeek(year,month,day):
    months=[3,0,3,2,3,2,3,3,2,3,2,3]
    cntYear=1900
    cntMonth=1
    cntDOW=1
    while(cntYear<year):
        cntYear=cntYear+1
        cntDOW=cntDOW+1
        if(cntYear%4 or ((cntYear%100==0) and cntYear%400)):
            cntDOW=cntDOW+1
    while(cntMonth<month):
        if(cntMonth!=2 or (cntYear%4 or ((cntYear%100==0) and cntYear%400))):
            cntDOW=cntDOW+months[cntMonth-1]
        else:
            cntDOW=cntDOW+1
        cntMonth=cntMonth+1
    cntDOW=(cntDOW+day-1)%7
    return ["sun","mon","tue","wed","thu","fri","sat"][cntDOW]

for y in range(1960,2000):
    print(y,dayOfWeek(y,m,d))

