# from collections import deque
#
# def solution(n,computers):
#     answer = 0
#     visited = [False for _ in range(n)]
#     for i in range(n):
#         if visited[i] == False:
#             visited[i]=True
#             queue = deque([i])
#             print(queue)
#             answer += 1
#         while queue:
#             idx = queue.popleft()
#             visited[idx]=True
#             for j in range(len(computers[idx])):
#                 if visited[j] == False and computers[idx][j] == 1:
#                     queue.append(j)
#     return answer


# def solution(n, computers):
#     cnt=0
#     answer=0
#     visited=[0 for i in range(n)]
#     def dfs(i):
#         for j in range(n):
#                 if computers[i][j] and not visited[j]:
#                     visited[j]=1
#                     dfs(j)
#
#     for i in range(n):
#         if not visited[i]:
#             visited[i]=1
#             dfs(i)
#             cnt+=1
#     answer=cnt
#
#     return answer

# from collections import deque


# def solution(n, computers):
#     answer = 0
#     tree = {}
#     visit = [0 for i in range(n + 1)]
#     for i in range(n):
#         for nn, j in enumerate(computers[i]):
#             if j == 1 and nn == i or j == 0:
#                 continue
#             elif i + 1 in tree:
#                 tree[i + 1].append(nn + 1)
#             else:
#                 tree[i + 1] = [nn + 1]
#
#     def bfs(i):
#         print(i)
#         visit[i] = 1
#         if i in tree:
#             dq = deque([i])
#             while dq:
#                 x = dq.pop()
#                 for j in tree[x]:
#                     if visit[j] == 0:
#                         dq.append(j)
#                         visit[j] = 1
#
#     for i in range(1, n + 1):
#         if visit[i] == 0:
#             bfs(i)
#             answer += 1
#     return answer