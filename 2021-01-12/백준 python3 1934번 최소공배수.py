def gcd(m,n):
    if m==0 or n==0:
        return (m if n==0 else n)
    elif m>n:
        a=m%n
        return gcd(n,a)
    elif m<n:
        a=n%m
        return gcd(m,a)

for x in range(int(input())):
    a,b=map(int,input().split())
    if a==b:
        print(a)
    else:
        k=gcd(a,b)
        print((a*b)//k)
