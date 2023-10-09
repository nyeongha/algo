from collections import deque

def solution(n,computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            visited[i]=True
            queue = deque([i])
            print(queue)
            answer += 1
        while queue:
            idx = queue.popleft()
            visited[idx]=True
            for j in range(len(computers[idx])):
                if visited[j] == False and computers[idx][j] == 1:
                    queue.append(j)
    return answer