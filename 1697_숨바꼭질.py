import sys
from collections import deque
visit=[0 for i in range(200001)]

n,k=map(int,sys.stdin.readline().split())

def bfs(n):
    q=deque([n])
    while q:
        x=q.popleft()
        l=[x-1,x+1,2*x]
        if x==k:
            return print(visit[x])
        for i in l:
            if 0<=i<=100000:
                if not visit[i]:
                    visit[i]=visit[x]+1
                    q.append(i)
                
        
bfs(n)

