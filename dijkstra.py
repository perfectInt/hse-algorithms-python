import heapq

n, m, s = map(int, input().split())
graph = [[] for i in range(n)]
INF = 2 ** 20
dist = [INF] * n
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append([v - 1, w])


def dijkstra(start):
    global dist, graph
    dist[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return dist


print(*dijkstra(s - 1))



