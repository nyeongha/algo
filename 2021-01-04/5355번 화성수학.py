for x in range(int(input())):
    i=list(input().split())
    z=0
    for y in i:
        if y=='@':
            z*=3
        elif y=='%':
            z+=5
        elif y=='#':
            z-=7
        else:
            z+=float(y)
    print('%.2f'%z)