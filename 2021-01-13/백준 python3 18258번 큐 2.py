from collections import deque
import sys
arr = deque()
for x in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().split()
    if len(a)==2:
        if a[0]=='push':
            arr.appendleft(a[1])
    if len(a)==1:
        if a[0]=='pop':
            if arr:
                print(arr.pop())
            else:
                print(-1)
        elif a[0] == 'size':
            print(len(arr))
        elif a[0] == 'empty':
            if not arr:
                print(1)
            else:
                print(0)
        elif a[0] == 'front':
            if arr:
                print(arr[-1])
            else:
                print(-1)
        elif a[0] == 'back':
            if arr:
                print(arr[0])
            else:
                print(-1)




