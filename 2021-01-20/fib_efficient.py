def fib_ef(n):
    f=[0]*(n+1)
    if n>0:
        f[1]=1
        for x in range(2,n+1):
            f[x]=f[x-1]+f[x-2]
    return f[n]


for i in range(11):
    print(fib_ef(i),end=' ')