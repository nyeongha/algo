def jsw(n):
    b={}
    for x in n:
        b[x]=n.count(x)
    if len(b)==3:
            t=sorted(n)
            return (t[2]*100)
    else:
        for x in b:
            if b[x]==3:
                return (10000+x*1000)
                break
            elif b[x]==2:
                return (1000+x*100)
arr=[]
for x in range(int(input())):
    a=list(map(int,input().split()))
    arr.append(jsw(a))
c=sorted(arr)
print(c[len(c)-1])