import sys
from collections import deque

N,M,V=map(int,sys.stdin.readline().split())
# 정점의 개수 N, 간선의 개수 M,탐색을 시작할 정점의 번호 V

L=[[] for i in range(N+1)]

visit=[0]*(N+1)

for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    if b not in L[a]:
        L[a].append(b)
    if a not in L[b]:
        L[b].append(a)

def dfs(v):
    visit[v]=1
    print(v,end=' ')
    L[v].sort()
    for i in L[v]:
        if visit[i]==0:
            dfs(i)

visit1=[0]*(N+1)
def bfs(v):
    q = deque([v])
    while q:
        a=q.popleft()
        print(a,end=' ')
        visit1[a]=1
        L[a].sort()
        for i in L[a]:
            if visit1[i]==0:
                q.append(i)
                visit1[i]=1



dfs(V)
print()
bfs(V)

            

