arr=str(input())
k=10
for x in range(1,len(arr)):
    if arr[x-1]==arr[x]:
        k+=5
    else:
        k+=10
print(k)