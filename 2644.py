def dfs(graph, start, end):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex == end:
            return path
        for neighbor in graph[vertex]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))
    return -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = dfs(graph, start, end)
print(len(result)-1 if result != -1 else -1)
