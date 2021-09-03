from collections import deque

a, b, c = map(int, input().split())
gr = {}
for x in range(b):
    m, n = map(int, input().split())
    if m not in gr:
        gr[m] = []
    if n not in gr:
        gr[n] = []
    if n not in gr[m]:
        gr[m].append(n)
    if m not in gr[n]:
        gr[n].append(m)

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        pn = stack.pop()
        if pn not in visited:
            visited.append(pn)
            temp = list(i for i in gr[pn] if i not in visited)
            temp.sort(reverse=True)
            stack += temp
    return visited


def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        pn2 = queue.popleft()
        if pn2 not in visited:
            visited.append(pn2)
            temp = list(i for i in graph[pn2] if i not in visited)
            temp.sort()
            queue.extend(temp)
    return visited


print(' '.join(map(str, dfs(gr, c))))
print(' '.join(map(str, bfs(gr, c))))
