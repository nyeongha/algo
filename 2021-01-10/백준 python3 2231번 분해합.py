n = int(input())
x = 0
for i in range(1, n+1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if s==n:
        print(i)
        break
    elif i==n:
        print(0)