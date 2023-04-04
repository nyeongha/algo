from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

# 너비 우선 탐색
def bfs(x, y):
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]

    q=deque()
    q.append((x,y))

    while q:
        # print(q)
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if (nx<0) or (ny<0) or (nx>N-1) or (ny>M-1):
                continue

            if graph[nx][ny]==0:
                continue

            elif graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                # for j in graph:
                #     print(*j,end='\n')
                q.append((nx,ny))

    return graph[N-1][M-1]

print(bfs(0, 0))