# https://acmp.ru/index.asp?main=task&id_task=135
n = int(input())
graph = [] * n
for i in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    print(*graph[i])
