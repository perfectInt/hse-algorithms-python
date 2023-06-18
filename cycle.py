n, m = map(int, input().split())
graph = [[] for i in range(n)]
used = [0] * n
path = []
ans = []

# Graph initialization
for i in range(m):
    s, f = map(int, input().split())
    s -= 1
    f -= 1
    graph[s].append(f)


def dfs(v: int) -> None:
    global ans, path
    used[v] = 1
    path.append(v)
    for edge in graph[v]:
        if used[edge] == 1:
            ans = path[:] + [edge]
        elif used[edge] == 0:
            dfs(edge)
    used[v] = 2
    path.pop()


for i in range(n):
    if used[i] == 0:
        dfs(i)

if len(ans) > 0:
    print("Has cycle.")
    idx = ans.index(ans[-1])
    ans = ans[idx:]
    print(*[i + 1 for i in ans])
else:
    print("No cycle")
