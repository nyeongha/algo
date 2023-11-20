from functools import reduce
arr=[]
for x in range(5):
    arr.append(int(input()))
    if arr[x]<=40:
        arr[x]=40
k=reduce(lambda x,y:x+y,arr)
print(k//5)