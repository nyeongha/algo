graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        print(n)
        if n not in visited:
            visited.append(n)
            print('graph[n]:',graph[n])
            print('set(visited):',set(visited))
            queue += graph[n] - set(visited)
            print('queue:',queue)
    return visited
print(bfs(graph,'A'))
