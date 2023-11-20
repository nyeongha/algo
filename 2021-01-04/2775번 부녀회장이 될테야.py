for x in range(int(input())):
    arr=[]
    c=1
    a=int(input())
    b=int(input())
    for y in range(a+1):
        arr.append([])
        for z in range(b):
            if y==0:
                arr[y].append(c)
                c+=1
            else:
                k=0
                for i in range(z+1):
                    k+=arr[y-1][i]
                arr[y].append(k)
    print(arr[a][b-1])