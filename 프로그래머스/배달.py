
import heapq
IN F =int(1e9)

def dijjkstra(graph ,N):
    q = [(0, 1)]
    distance = [INF for i in range( N +1)]
    distance[1 ] =0


    while q:
        n_dist, n_node = heapq.heappop(q)


        if n_dist > distance[n_node]:
            continue

        for ad_node, an_dist in graph[n_node]:
            tot = an_dist + n_dist

            if tot < distance[ad_node]:
                distance[ad_node] = tot
                heapq.heappush(q, (distance[ad_node], ad_node))

    return distance
def solution(N, road, K):
    answer =0
    graph = {}
    for a, b, c in road:
        if a in graph:
            graph[a].append((b, c))
        else \
            :graph[a ] =[(b ,c)]
        if b in graph:
            graph[b].append((a ,c))
        else \
            :graph[b ] =[(a ,c)]
    tb =dijjkstra(graph ,N)

    for i in tb[1:]:
        if i<= K:
            answer += 1

    return answer