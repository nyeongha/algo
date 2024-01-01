from heapq import heappush, heappop
import sys
input = sys.stdin.readline
hq=[]

for i in range(int(input())):
    x=(int(input()))
    if x:
        heappush(hq,(abs(x),x))
    else:
        if not hq:
            print(0)
        else:
            n=heappop(hq)
            print(n[1])
