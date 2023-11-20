c=[]
a=1
b=1
while a!=0 and b!=0:
    a,b=map(int,input().split())
    if a!=0 and b!=0:
        c.append(a+b)
for x in c:
    print(x)