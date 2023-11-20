for x in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif ((x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 - r2) ** 2) or (r1 + r2) ** 2 < (x1 - x2) ** 2 + (y1 - y2) ** 2:
        print(0)
    elif ((r1 + r2) ** 2 == (x1 - x2) ** 2 + (y1 - y2) ** 2) or ((x1 - x2) ** 2 + (y1 - y2) ** 2 == (r1 - r2) ** 2):
        print(1)
    else:
        print(2)