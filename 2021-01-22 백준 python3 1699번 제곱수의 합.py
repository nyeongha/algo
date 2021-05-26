import math
n = int(input())
t = 0
flag = True
while n != 0:

    b = math.floor(n ** 0.5)
    for x in range(b, 1, -1):
        if n % (x ** 2) == 0:
            t = n // (x ** 2)
            flag = False
            break
        else:
            continue
    if not flag:
        break
    elif flag:
        n -= (b ** 2)
        t += 1
print(t)
