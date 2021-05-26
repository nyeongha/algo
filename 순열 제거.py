import itertools
a=int(input())
arr=[]
for x in range(a):
    arr.append(input())

for i,x in enumerate(arr):
    result = list(map(''.join,itertools.permutations(x)))
    for y in arr[i+1:]:
        if y in result:
            arr.remove(y)
arr.sort()
for k in arr:
    print(k,end='\n')



