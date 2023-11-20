from functools import reduce

arr = []
for x in range(int(input()), int(input()) + 1):
    if x == 1:
        continue
    elif x == 2:
        arr.append(x)
    else:
        for y in range(2, x):
            if x % y == 0:
                break
            elif x == y + 1:
                arr.append(x)

if len(arr) == 0:
    print(-1)
else:
    b = reduce(lambda x, y: x + y, arr)
    print(b)
    print(arr[0])