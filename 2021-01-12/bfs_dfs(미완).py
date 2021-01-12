from collections import deque


def dfs(start):
    visited = []
    stack = [start]

    while stack:
        pn = stack.pop()
        print(pn)
        if pn not in visited:
            visited.append(pn)
            print(visited)
            temp = list(i for i in gr[pn] if i not in visited)
            temp.sort(reverse=True)
            stack += temp
            print(stack)
    return visited


def bfs(start):
    visited = []
    queue = deque([start])
    while queue:
        pn2 = queue.popleft()
        print(pn2)
        if pn2 not in visited:
            visited.append(pn2)
            print(visited)
            temp = list(i for i in gr[pn2] if i not in visited)
            temp.sort()
            queue.extend(temp)
            print(queue)
    return visited


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

print(' '.join(map(str, dfs(c))))
print(' '.join(map(str, bfs(c))))
