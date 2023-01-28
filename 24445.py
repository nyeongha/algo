from collections import deque
import sys
input = sys.stdin.readline


V,E,R=map(int,input().split())
visited=[0]*(V+1)
adl=[[] for _ in range(V+1)]
cnt=1

for _ in range(E):
    m,n=map(int,input().split())
    adl[m].append(n)
    adl[n].append(m)
    
for x in adl:
    x.sort(reverse=True)    
    
def bfs(R):
    global cnt
    a=deque([R])
    visited[R]=cnt
    while a:
        b=a.popleft()
        for i in adl[b]:
            if visited[i]==0:
                cnt+=1
                visited[i]=cnt
                a.append(i)

bfs(R)
for k in visited[1:]:
    print(k)
    
                    
    