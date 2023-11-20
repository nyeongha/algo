arr=[]
for _ in range(10):
    arr.append(int(input()))

k=0
for x in arr:
    arr[k]=x%42
    k+=1
set_arr=set(arr)
print(len(set_arr))