# 수빈이가 있는 위치 N
# 동생이 있는 위치 K
# (0 ≤ N ≤ 100,000)


from collections import deque

N,K=map(int,input().split())
visit=[0 for _ in range(100001)]

def bfs():
    q=deque([N])
    visit[N]=1
    while q:
        x=q.popleft()
        if x==K:
            return print(visit[K]-1)
        if 0<=2*x<=100000 and visit[2*x]==0:
            visit[2*x]=visit[x]
            q.append(2*x)
        for i in [x-1,x+1]:
            if 0<=i<=100000 and visit[i]==0:
                visit[i]=visit[x]+1
                q.append(i)
        



bfs()