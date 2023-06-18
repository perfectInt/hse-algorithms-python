n, m = map(int, input().split())
graph = [[] for i in range(n)]
used = [0] * n
tin = [0] * n
up = [0] * n
timer = 0
ans = []

# Graph initialization
for i in range(m):
    s, f = map(int, input().split())
    s -= 1
    f -= 1
    graph[s].append(f)
    graph[f].append(s)


def dfs(v: int, p: int = -1) -> None:
    global used, tin, up, timer, ans
    timer += 1
    tin[v] = up[v] = timer
    used[v] = 1
    for edge in graph[v]:
        if edge == p:
            continue
        if used[edge] == 0:
            dfs(edge, v)
            up[v] = min(up[edge], up[v])
            if up[edge] > tin[v]:
                ans.append([v, edge])
        else:
            up[v] = min(up[v], tin[edge])


for i in range(n):
    if used[i] == 0:
        dfs(i)

print(*ans)
