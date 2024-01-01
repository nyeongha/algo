from heapq import heappush, heappop
import sys
input = sys.stdin.readline
hq=[]

for i in range(int(input())):
    heappush(hq,int(input()))
cnt=0
while len(hq)!=1:
    a=heappop(hq)
    b=heappop(hq)
    cnt+=(a+b)
    heappush(hq, a + b)

print(cnt)
