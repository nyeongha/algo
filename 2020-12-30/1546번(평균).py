from functools import reduce
i=int(input())
arr=[]
arr[0:i]=map(int,input().split())
arr.sort()
k=0
for x in arr:
    arr[k]=x/arr[i-1]*100
    k+=1
o=reduce(lambda x,y:x+y,arr)
print(o/i)