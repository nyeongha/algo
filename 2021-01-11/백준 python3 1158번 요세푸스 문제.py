from collections import deque
n,k=map(int,input().split())
arr=deque()
for x in range(1,n+1):
    arr.append(x)
arr2=[]
for y in range(n):
    arr.rotate(-(k-1))
    arr2.append(arr[0])
    arr.remove(arr[0])
print('<{}>'.format(', '.join(map(str,arr2))))