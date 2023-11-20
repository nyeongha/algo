a = list(map(int, input().split()))
b = {}
for x in a:
    b[x] = a.count(x)
if len(b) == 3:
    t = sorted(a)
    print(t[2] * 100)
else:
    for x in b:
        if b[x] == 3:
            print(10000 + x * 1000)
            break
        elif b[x] == 2:
            print(1000 + x * 100)



