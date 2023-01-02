V,M,R=map(int,input().split())
adj=[[0]*V for i in range(V+1)]
visited=[False]*(V)

for _ in range(M):
    m,n=map(int,input().split())
    adj[m][n]=1
    adj[n][m]=1

def dfs(x):
    visited[x]=True
    print(x)
    for _ in range(5):
        if (adj[x][_]==1) and visited[_]==False:
            dfs(_)
        elif visited[_]==False:print(0)
            
            
dfs(1)