import math
i=int(input())
for x in range(i):
    h,w,n=map(int,input().split())
    b=str(math.ceil(n/h))
    a=n-(h*(math.ceil(n/h)-1))
    zero_b=b.zfill(2)
    print('%s%s'%(a,zero_b))