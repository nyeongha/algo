from collections import deque

N=int(input())

canvas=[]
for i in range(N):
    canvas.append(list(str(input())))




def dfs(x,y,color):
    q=deque([(x,y)])
    while q:
        m,n=q.popleft()
        if color=='B':
            visit[x][y]=1
        if color=='R' or color=='G':
            visit[x][y]=-1
        for i,j in [(m+1,n),(m-1,n),(m,n+1),(m,n-1)]:
            if 0<=i<N and 0<=j<N:
                if visit[i][j]==0 and canvas[i][j]==color:
                    if color=='B':
                        q.append((i,j))
                        visit[i][j]=1
                    elif color=='R' or color=='G':
                        q.append((i,j))
                        visit[i][j]=-1



def d(x,y):
    qq=deque([(x,y)])
    visit[x][y]=1
    while qq:
        m,n=qq.popleft()
        for i,j in [(m+1,n),(m-1,n),(m,n+1),(m,n-1)]:
            if 0<=i<N and 0<=j<N:
                if visit[i][j]==-1:
                    qq.append((i,j))
                    visit[i][j]=1


B_cnt=0
R_cnt=0
G_cnt=0
RG_cnt=0
visit=[[0 for _ in range(N)] for __ in range(N)]
for x in range(N):
    for y in range(N):
        if canvas[x][y]=='B' and visit[x][y]==0:
            dfs(x,y,'B')
            B_cnt+=1
        if canvas[x][y]=='R'and visit[x][y]==0:
            dfs(x,y,'R')
            R_cnt+=1
        if canvas[x][y]=='G'and visit[x][y]==0:
            dfs(x,y,'G')
            G_cnt+=1


for x in range(N):
    for y in range(N):
        if visit[x][y]==-1:
            d(x,y)
            RG_cnt+=1

print(R_cnt+G_cnt+B_cnt,B_cnt+RG_cnt)





            