
from collections import deque

# M은 상자의 가로 칸의 수, N은 상자의 세로 칸
# 정수 1은 익은 토마토
# 정수 0은 익지 않은 토마토
# 정수 -1은 토마토가 들어있지 않은 칸
M,N=map(int,input().split())
box=[]
visit=[[0 for ii in range(M)] for jj in range(N)]



for _ in range(N):
    box.append(list(map(int,input().split())))


def bfs():
    while q:
        x,y=q.popleft()
        for xx,yy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=xx<N and 0<=yy<M and not visit[xx][yy]:
                if box[xx][yy]==0:
                    visit[xx][yy]=visit[x][y]+1
                    q.append((xx,yy))
                if box[xx][yy]==-1:
                    visit[xx][yy]=1
    
                
    



q=deque()
for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            q.append((i,j))
            visit[i][j]=1
        if box[i][j]==-1:
            visit[i][j]=-1

bfs()

max=0
for iii in range(N):
    for jjj in range(M):
        if max<visit[iii][jjj]:
            max=visit[iii][jjj]
        if visit[iii][jjj]==0:
            print(-1)
            exit()
print(max-1 if max!=1 else 0)


            
