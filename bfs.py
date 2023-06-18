# https://acmp.ru/index.asp?main=task&id_task=127
import queue

n = int(input())
graph = []
q = queue.Queue()
visited = [0] * n
for i in range(n):
    graph.append(list(map(int, input().split())))
s, f = map(int, input().split())
s -= 1
f -= 1

q.put(s)
visited[s] = 1

while not q.empty():
    v = q.get()
    for i in range(n):
        if graph[v][i] == 1 and visited[i] == 0:
            visited[i] = visited[v] + 1
            q.put(i)


if visited[f] != 0:
    print(visited[f] - 1)
else:
    print(-1)

