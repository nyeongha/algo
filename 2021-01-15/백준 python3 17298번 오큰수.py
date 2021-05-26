import sys
a=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
ar=[-1 for _ in range(a)]
stc=[]
for _ in range(a):
    if _!=a-1 and arr[_]<arr[_+1]:
        ar[_]=arr[_+1]
        while stc and arr[stc[-1]] < ar[_]:
            ar[stc[-1]]=ar[_]
            stc.pop()
    else:
        stc.append(_)
print(*ar)
