from collections import deque
def solution(maps):
    answer=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    d=deque([(0,0)])
    n=len(maps) #층,세로
    m=len(maps[0])  #가로
    visited=[[0 for j in range(m)] for i in range(n)]
    visited[0][0]=1
    while d:
        a,b=d.popleft()
        for x,y in zip(dx,dy):
            xx,yy=a+x,b+y
            if 0<=xx<n and 0<=yy<m:
                if maps[xx][yy]==1 and visited[xx][yy]==0:
                    visited[xx][yy]=1
                    maps[xx][yy]=maps[a][b]+1
                    d.append((xx,yy))
    answer=-1 if maps[n-1][m-1]==1 else maps[n-1][m-1]
    return answer