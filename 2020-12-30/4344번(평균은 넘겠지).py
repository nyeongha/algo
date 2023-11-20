from functools import reduce
i=int(input())
arr=[]
for x in range(i):
    arr.append([])
#print(arr)

for y in range(i):
    arr[y][0:]=map(int,input().split())
#print(arr)

from functools import reduce
for x in arr:
    y=reduce(lambda a,b:a+b,x[1:])
    ag=0
    for _ in x[1:]:
        if _>y/x[0]:
            ag+=1
    print("%.3f%%"%(ag/x[0]*100))