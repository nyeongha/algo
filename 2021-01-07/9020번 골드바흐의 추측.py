#%%
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]
for x in range(int(input())):
    arr=[]
    a=int(input())
    k=prime_list(a)
    t=[i for i in k if i<=(a//2)]
    b=[i for i in k if i>=a//2]
    for _ in reversed(t):
        for c in b:
            if _+c==a:
                print(_,c)
                break
        if _+c==a:
            break