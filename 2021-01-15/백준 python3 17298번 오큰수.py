# import sys
# from collections import deque
# a=int(sys.stdin.readline())
# arr=deque(list(map(int, sys.stdin.readline().split())))
# st=[-1]*a
# cnt=0
# while arr:
#     x=arr.popleft()
#     if len(arr)==0:
#         break
#     for i in arr:
#         if i>x:
#             st[cnt]=i
#             break
#     cnt+=1
# print(*st)

import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
NGE = [-1] * n
stack = [0]
for i in range(1,n):
    while stack and A[stack[-1]]<A[i]:
        NGE[stack.pop()]=A[i]
    stack.append(i)
print(*NGE)