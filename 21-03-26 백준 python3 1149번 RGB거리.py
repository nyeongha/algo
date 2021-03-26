arr=[]
for x in range(int(input())):
    arr.append(list(map(int,input().split())))
for y in range(1,len(arr)):
    arr[y][0]+= min(arr[y-1][1],arr[y-1][2])
    arr[y][1]+= min(arr[y - 1][0], arr[y - 1][2])
    arr[y][2]+= min(arr[y - 1][0], arr[y - 1][1])
print(min(arr[len(arr)-1][0],arr[len(arr)-1][1],arr[len(arr)-1][2]))