n = int(input())
han = 0
for i in range(1, n + 1):
    if i < 100:
        han += 1
    else:
        ns =list(str(i))
        ns =list(map(int,ns))
        if (ns[0] - ns[1] == ns[1] - ns[2]):
            han += 1
print(han)