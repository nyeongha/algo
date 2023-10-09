from collections import deque


# 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)
n,m=map(int,input().split())
art_num=0

one_num=[0]

visit=[[0 for i in range(m)] for j in range(n)]
canvas=[]


for _ in range(n):
    canvas.append(list(map(int,input().split())))



def bfs(a,b):
    on=0
    q=deque([(a,b)])
    
    while q:
        x,y=q.popleft()
        visit[x][y]=1
        for sero,garo in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=sero<n and 0<=garo<m and canvas[sero][garo]==1 and not visit[sero][garo]:
                visit[sero][garo]=1
                on+=1
                q.append((sero,garo))
                
    return on

for i in range(n):
    for j in range(m):
        if canvas[i][j]==1 and not visit[i][j]:
            one_num.append(bfs(i,j)+1)
            art_num+=1

print(art_num)
print(max(one_num))
