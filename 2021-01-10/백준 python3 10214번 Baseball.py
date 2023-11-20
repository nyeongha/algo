for i in range(int(input())):
    a = 0
    b = 0
    for x in range(9):
        m, n = map(int, input().split())
        a += m
        b += n
    if a > b:
        print('Yonsei')
    elif a < b:
        print('Korea')
    else:
        print('Draw')


