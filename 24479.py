import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V,M,R=map(int,input().split())
adj=[[] for i in range(V+1)]
visited=[0]*(V+1)
v=[0]*(V+1)
cnt=1

for _ in range(M):
    m,n=map(int,input().split())
    adj[m].append(n)
    adj[n].append(m)

    
def dfs(x):
    global cnt
    visited[x]=cnt
    adj[x].sort()
    for i in adj[x]:
        if not visited[i]:
            cnt+=1
            dfs(i)

dfs(R)
for x in range(1,V+1):
    print(visited[x])