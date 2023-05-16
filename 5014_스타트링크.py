from collections import deque

F, S, G, U, D=map(int,input().split())
visit=[0 for i in range(F+1)]




def bfs(s):
    q=deque([s])
    visit[s]=1
    while q:
        x=q.popleft()
        if x==G:
            return print(visit[x]-1)
        
        for i in [x+U,x-D]:
            if 1<=i<=F and not visit[i]:
                visit[i]=visit[x]+1
                q.append(i)

    return print("use the stairs")


bfs(S)