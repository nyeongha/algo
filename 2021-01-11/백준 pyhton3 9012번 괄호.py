
for x in range(int(input())):
    arr=[]
    a=list(str(input()))
    flag=True
    for _ in a:
        if _ =='(':
            arr.append('(')
        elif _ ==')':
            if '(' in arr:
                arr.pop()
            elif '(' not in arr:
                flag=False
                print('NO')
                break
    if arr and flag==True:
            print('NO')
    elif not arr and flag==True:
            print('YES')