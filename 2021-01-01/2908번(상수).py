from functools import reduce
i=input().split()
k=[]
for x in i:
    p=list(str(x))
    k.append(p)
a=[]
for t in range(len(k)):
    a.append(reduce(lambda x,y:y+x,k[t]))
if int(a[0])>int(a[1]):
    print(a[0])
else:
    print(a[1])