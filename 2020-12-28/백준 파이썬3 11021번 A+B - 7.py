def hap(x, y):
    return x + y


i = int(input())

c = [[0 for j in range(2)] for i in range(i)]
d = []
for a, b in c:
    a, b = map(int, input().split())
    d.append(hap(a, b))
x = 1
for i in d:
    print('Case #%d:' % x, i)
    x += 1