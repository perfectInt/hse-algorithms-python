n, m = map(int, input().split())
graph = [[] for i in range(n)]
used = [0] * n
path = []

# Graph initialization
for i in range(m):
    s, f = map(int, input().split())
    s -= 1
    f -= 1
    graph[s].append(f)
    graph[f].append(s)


def dfs(v: int) -> None:
    used[v] = 1
    path.append(v)
    for edge in graph[v]:
        if used[edge] == 0:
            dfs(edge)


for i in range(n):
    if used[i] == 0:
        dfs(i)

print(*[x + 1 for x in path])
