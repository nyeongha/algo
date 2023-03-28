# import sys
#
# n=(str(sys.stdin.readline().strip()))
# visited=[0]*len(n)
# s=[]
# y=[]
#
# def dfs():
#     if len(n)==len(s):
#         y.append(int(''.join(s)))
#         return
#
#     for i in range(len(n)):
#         if visited[i]==0:
#             s.append(n[i])
#             visited[i]=1
#             dfs()
#             s.pop()
#             visited[i]=0
#
# dfs()
# y.sort()
# for x in y:
#     if x > int(n):
#         print(x)
#         exit()
# print(0)



import sys
from itertools import permutations
n=str(sys.stdin.readline().strip())
k=permutations(n)
kk=[]
v=[0]*len(n)
for v in k:
    kk.append(''.join(v))
c=list(map(int,kk))
c.sort()
for x in c:
    if x > int(n):
        print(x)
        exit()
print(0)