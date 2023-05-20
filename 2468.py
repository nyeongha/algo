from collections import deque
# 2차원 배열의 행과 열의 개수를 나타내는 수 N
N=int(input())
height=[]
for i in range(N):
    height.append(list(map(int,input().split())))
    

def dfs(x,y):
    q=deque([(x,y)])
    visit[x][y]=1
    while q:
        m,n=q.popleft()
        for mm,nn in [(m+1,n),(m-1,n),(m,n+1),(m,n-1)]:
            if 0<=mm<N and 0<=nn<N:
                if not visit[mm][nn]:
                    q.append((mm,nn))
                    visit[mm][nn]=1


height_range=[]
for i in height:
    for j in i:
        if j not in height_range:
            height_range.append(j)

height_range.sort()

cnt_list=[]

for ii in height_range:
    visit=[[0 for i in range(N)] for j in range(N)]
    cnt=0
    for a in range(N):
        for b in range(N):
            if height[a][b]<=ii:
                visit[a][b]=1


    for x in range(N):
        for y in range(N):
            if visit[x][y]==0:
                dfs(x,y)
                cnt+=1 
    cnt_list.append(cnt)


print(max(cnt_list) if max(cnt_list)!=0 else 1)
