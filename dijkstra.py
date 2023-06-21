import heapq

n, m, s = map(int, input().split())
edges = []
INF = 2 ** 20
dist = [INF] * n
visited = [False] * n
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))
dist[s - 1] = 0


def dijkstra(edges, start_vertex):
    global visited, dist
    edge_list = []
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]].append([edge[1], edge[2]])
    visited[start_vertex] = True
    dist[start_vertex] = 0
    for dest, weight in graph[start_vertex]:
        heapq.heappush(edge_list, (weight, start_vertex, dest))
    while len(edge_list) > 0:
        weight, src, dest = heapq.heappop(edge_list)
        if visited[dest]:
            continue
        dist[dest] = dist[src] + weight
        visited[dest] = True
        for new_dest, new_weight in graph[dest]:
            if not visited[new_dest]:
                heapq.heappush(edge_list, (new_weight, dest, new_dest))
    return dist


print(*dijkstra(edges, s - 1))



