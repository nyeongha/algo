n,m=map(int,input().split())
ar=[]
br=[]
arr=list(map(int,input().split()))

for x in arr:
    for y in arr[arr.index(x)+1:]:
        for z in arr[arr.index(y)+1:]:
            if (x+y+z)<=m:
                ar.append(x+y+z)
ar.sort()
print(ar[-1])

