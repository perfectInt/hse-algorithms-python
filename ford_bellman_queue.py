import queue

n, m = map(int, input().split())
graph = [[] for i in range(m)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append([v - 1, w])
dist = [30000] * n
q = queue.Queue()

dist[0] = 0
q.put(0)
is_in_queue = [False] * n
is_in_queue[0] = True

while not q.empty():
    v = q.get()
    is_in_queue[v] = False

    for u, w in graph[v]:
        if dist[v] + w < dist[u]:
            dist[u] = dist[v] + w
            if not is_in_queue[u]:
                q.put(u)
                is_in_queue[u] = True

print(*dist)
