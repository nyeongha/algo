i=int(input())
arr=['' for x in range(i)]
a=0
for x in range(i):
    y,k=map(str,input().split())
    for _ in k:
        arr[a]+=_*int(y)
    a+=1
for _ in arr:
    print(_)