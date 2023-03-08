import heapq
import sys

heap = []

for i in range(int(sys.stdin.readline())):
    a=int(sys.stdin.readline())
    if a>=1:
        heapq.heappush(heap,-a)
    elif a==0:
        if len(heap)==0:
            print(0)
        else:
            print(-(heapq.heappop(heap)))