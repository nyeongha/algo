s=input()
up=list(s.upper())
set_up=list(set(up))
se=[]
for _ in set_up:
    line=[]
    for x in _:
        line.append(_)
        line.append(0)
    se.append(line)
ss=0
for x,y in se:
    for c in up:
        if x==c:
            y+=1
            se[ss][1]=y
    ss+=1
k=sorted(se, key=lambda x:x[1])
if len(k)>1 and k[len(k)-1][1]==k[len(k)-2][1]:
    print('?')
else:
    print(k[len(k)-1][0])