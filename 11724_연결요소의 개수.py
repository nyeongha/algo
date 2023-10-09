from collections import deque
import sys
input=sys.stdin.readline



N,M=map(int,input().split())
dq=[[] for _ in range(N+1)]
visit=[False]*(N+1)

for i in range(M):
    u,v=map(int,input().split())
    dq[u].append(v)
    dq[v].append(u)



def bfs(val):
    q=deque([val])
    visit[val]=True
    while q:
        x=q.popleft()
        for i in dq[x]:
            if not visit[i]:
                q.append(i)
                visit[i]=True

cnt=0
for ii in range(1,N+1):
    if not visit[ii]:
        bfs(ii)
        cnt+=1

print(cnt)

