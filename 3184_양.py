from collections import deque

# 글자 '.' (점)은 빈 필드
# 글자 '#'는 울타리
# 'o'는 양
# 'v'는 늑대

R,C=map(int,input().split())
field=[]
visit=[[0 for ii in range(C)] for jj in range(R)]

num=[0,0] # 양,늑대

for r in range(R):
    field.append(list(str(input())))


def bfs(i,j):
    v=0
    o=0
    q=deque([(i,j)])

    while q:
        x,y=q.popleft()
        for m,n in [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=m<R and 0<=n<C and not visit[m][n]:
                visit[m][n]=1
                if field[m][n]=='v':
                    v+=1
                    q.append((m,n))
                elif field[m][n]=='o':
                    o+=1
                    q.append((m,n))
                elif field[m][n]=='.':
                    q.append((m,n))
    

    if o>v:
        num[0]+=o
    else:
        num[1]+=v

    return num





for i in range(R):
    for j in range(C):
        if (field[i][j]=='v' or field[i][j]=='o' or field[i][j]=='.') and visit[i][j]==0:
            bfs(i,j)
            
print(*num,sep=' ')