import sys
from collections import deque

for i in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split()) # a문서의 갯수,b는 몇번째로 출력되는지 알고싶은 인덱스
    d=deque(map(int,sys.stdin.readline().split()))
    di=deque(range(a))
    cnt=0
    while d:
        if d[0]==max(d):
            cnt += 1
            d.popleft()
            if di[0]==b:
                print(cnt)
                break;
            else:
                di.popleft()
        else:
            d.append(d.popleft())
            di.append(di.popleft())



