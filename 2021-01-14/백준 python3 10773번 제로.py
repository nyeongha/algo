import sys
arr=[]
for x in range(int(sys.stdin.readline())):
    a=int(sys.stdin.readline())
    if a==0:
        if arr:
            arr.pop()
    else:
        arr.append(a)
print(sum(arr))
