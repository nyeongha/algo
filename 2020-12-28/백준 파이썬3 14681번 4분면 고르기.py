def Quadrant(x, y):
    if -1000 <= x < 0:
        if -1000 <= y < 0:
            print(3)
        else:
            print(2)
    else:
        if -1000 <= y < 0:
            print(4)
        else:
            print(1)


a, b = [int(input()) for x in range(2)]
Quadrant(a, b)