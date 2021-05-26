def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)


for x in range(11):
    print(fib(x),end=' ')