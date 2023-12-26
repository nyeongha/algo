def alarm(x, y):
    h = list(range(0, 24))
    m = list(range(0, 60))
    if 45 <= y:
        print(h[x], m[y - 45])
    else:
        print(h[x - 1], m[y - 45])


a, b = map(int, input().split())
alarm(a, b)