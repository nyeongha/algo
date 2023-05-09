from collections import deque


dx=[-1,1,0,0]
dy=[0,0,-1,1]


complex=[]
cnt=[]

n=int(input())

for i in range(n):
    complex.append(list(str(input())))



def bfs(x1,y1):
    cnt=0
    q=deque([(x1,y1)])
    complex[x1][y1]=0
    while q:
        x,y=q.pop()
        cnt+=1
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and complex[xx][yy]=='1':
                complex[xx][yy]=0
                q.append((xx,yy))
    return cnt
    


    

for x in range(n):
    for y in range(n):
        if complex[x][y]=='1':
            cnt.append(bfs(x,y))

print(len(cnt))
cnt.sort()
for _ in cnt:
    print(_)