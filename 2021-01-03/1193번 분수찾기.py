def dchx(i):
    x=0
    while True:
        if (1+x)/2*x<i:
            x+=1
        else:
            return x-1
def dch(k):
    return i-((1+a)/2*a)
i=int(input())
a=dchx(i)
b=0
c=0
d=dch(a)
if (a+1)%2==1:
    b=(a+2)-d
    c=d
else:
    b=d
    c=(a+2)-d
print('%d/%d'%(b,c))