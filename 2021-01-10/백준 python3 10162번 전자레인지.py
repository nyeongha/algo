i=int(input())
a=300
b=60
c=10
if i%10!=0:
    print(-1)
else:
    print(i//a,end=' ')
    print((i%a)//b,end=' ')
    print((i%b)//c)