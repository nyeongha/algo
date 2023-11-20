dic={'a':100,'b':100}
for x in range(int(input())):
    m,n=map(int,input().split())
    if m>n:
        dic['b']-=m
    elif m<n:
        dic['a']-=n
print(dic['a'])
print(dic['b'])