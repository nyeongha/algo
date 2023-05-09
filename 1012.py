from collections import deque
dx=[-1,1,0,0]#가로
dy=[0,0,-1,1]#세로



# 테스트 케이스의 개수 T
for T in range(int(input())):
    # 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
    m,n,k=map(int,input().split())
    field=[[0 for j in range(m)] for i in range(n)]
    for K in range(k):
        x,y=map(int,input().split())
        field[y][x]=1
        q=deque()

    def bfs(ii,jj):
        field[ii][jj]=0
        q.append((ii,jj))
        
        while q:
            ii,jj=q.pop()
            for x in range(4):
                xx=ii+dy[x]
                yy=jj+dx[x]
                if 0<=xx<n and 0<=yy<m and field[xx][yy]==1:
                    field[xx][yy]=0
                    q.append((xx,yy))
    


    cnt=0

    for i in range(n):#행
        for j in range(m):#열
            if field[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)
            
                
                




