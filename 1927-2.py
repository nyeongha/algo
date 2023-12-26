# import heapq
#
# ll=[]
# N=int(input())
# for _ in range(N):
#     x=int(input())
#     if x==0:
#         if len(ll)==0:
#             print(0)
#         else:
#             print(heapq.heappop(ll))
#     else:
#         heapq.heappush(ll,x)
#
#
import sys
import heapq

input = sys.stdin.readline

min_heap = []

for _ in range(int(input())):
    n = int(input())

    if n == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, n)