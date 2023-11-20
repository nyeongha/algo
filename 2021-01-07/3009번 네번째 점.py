x=[]
y=[]
for _ in range(3):
    a,b=map(int,input().split())
    if a not in x:
        x.append(a)
    elif a in x:
        x.remove(a)
    if b not in y:
        y.append(b)
    elif b in y:
        y.remove(b)
print(x[0],y[0])