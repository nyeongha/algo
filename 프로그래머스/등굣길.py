# from collections import deque
# def solution(m, n, puddles):
#     answer = 0
#     region=[[0 for i in range(m)] for j in range(n)]
#     ll=[]
#     dq=deque([(0,0)])
#     answer=0
#     while dq:
#         d=[(0,1),(1,0)]
#         x,y=dq.pop()
#         for xx,yy in d:
#             nx,ny=x+xx,y+yy
#             if nx==n-1 and ny==m-1:
#                 ll.append(region[x][y]+1)
#             if 0<=nx<n and 0<=ny<m:
#                 if [ny+1,nx+1] not in puddles:
#                     if region[nx][ny]>0:
#                         region[nx][ny]=region[x][y]+1
#                     dq.append([nx,ny])
#     answer=len(ll)%1000000007
#     return answer

# def solution(m, n, puddles):
#     answer = 0
#     region=[[0 for i in range(m+1)] for j in range(n+1)]
#     region[1][1]=1
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             if i==1 and j==1 or [j,i] in puddles:
#                 continue
#             else:
#                 region[i][j]=region[i-1][j]+region[i][j-1]
#     answer=region[n][m]
#     return answer

def solution(m, n, puddles):
    answer = 0
    region=[[0 for i in range(m+1)] for j in range(n+1)]
    region[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1 or [j,i] in puddles:
                continue
            else:
                region[i][j]=region[i-1][j]+region[i][j-1]
    answer=region[n][m]%1000000007
    return answer