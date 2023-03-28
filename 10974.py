import sys

n=int(sys.stdin.readline().strip())
visited=[0]*(n+1)
s=[]

def dfs():
    if len(s)==n:
        print(*s)
        return
    for i in range(1,n+1):
        if visited[i]==0:
            s.append(i)
            visited[i]
            dfs()
            s.pop()
            visited[i]=0
dfs()