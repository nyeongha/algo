import sys
n=int(sys.stdin.readline())
ar={}
arr=[]
for x in range(n):
    a=int(sys.stdin.readline())
    arr.append(a)
    if a not in ar:
        ar[a]=1
    else:
        ar[a]+=1
arr.sort()
print(round(sum(arr)/n)) #산술평균
print(arr[n//2]) #중앙값
max(ar,key=ar.get)
sr_ar=sorted([k for k,v in ar.items() if max(ar.values()) == v])
if len(sr_ar)==1:
    print(sr_ar[0])
else:print(sr_ar[1])
print(arr[len(arr)-1]-arr[0]) #범위
