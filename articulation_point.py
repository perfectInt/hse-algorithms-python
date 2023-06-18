n, m = map(int, input().split())
graph = [[] for i in range(n)]
used = [0] * n
points = set()
up = [0] * n
tin = [0] * n
timer = 0


# Graph initialization
for i in range(m):
    s, f = map(int, input().split())
    s -= 1
    f -= 1
    graph[s].append(f)
    graph[f].append(s)


def dfs(v: int, p: int = -1) -> None:
    global used, points, tin, up, timer
    timer += 1
    up[v] = tin[v] = timer
    used[v] = 1
    cnt = 0
    for edge in graph[v]:
        if edge == p:
            continue
        if used[edge] == 0:
            cnt += 1
            dfs(edge, v)
            up[v] = min(up[v], up[edge])
            if tin[v] <= up[edge] and p != -1:
                points.add(v)
        else:
            up[v] = min(up[v], tin[edge])
    if p == -1 and cnt > 1:
        points.add(v)


dfs(0)

print(points)
