import heapq
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


import heapq

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    q=[(0,start)]
    while q:
        n_dist,now_node=heapq.heappop(q)
        if distance[now_node]<n_dist:
            continue
        for ad_node,an_dist in graph[now_node].items():
            tot=n_dist+an_dist
            if tot<distance[ad_node]:
                distance[ad_node]=tot
                heapq.heappush(q,(distance[ad_node],ad_node))
    return distance
# def dijkstra(graph, start):
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#     queue = []
#     heapq.heappush(queue, [distances[start], start])
#
#     while queue:
#         current_distance, current_node = heapq.heappop(queue)
#
#         if distances[current_node] < current_distance:
#             continue
#
#         for adjacent, weight in graph[current_node].items():
#             distance = current_distance + weight
#
#             if distance < distances[adjacent]:
#                 distances[adjacent] = distance
#                 heapq.heappush(queue, [distance, adjacent])
#
#     return distances



print(dijkstra(mygraph, 'A'))

