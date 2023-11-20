import math
for x in range(int(input())):
    a,b=map(int,input().split())
    k=round(math.sqrt(b-a))
    if (k**2)-k+1<=(b-a)<=k**2:
        print(2*k-1)
    elif (k**2)+1<=(b-a)<=k**2+k:
        print(2*k)