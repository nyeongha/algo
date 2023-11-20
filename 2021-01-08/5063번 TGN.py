for x in range(int(input())):
    a,b,c=map(int,input().split())
    if a==b-c:
        print("does not matter")
    elif a>b-c:
        print('do not advertise')
    else:print('advertise')