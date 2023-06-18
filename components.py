n, m = map(int, input().split())
graph = [[] for i in range(n)]
used = [0] * n
components = [0] * n
count = 0

# Graph initialization
for i in range(m):
    s, f = map(int, input().split())
    s -= 1
    f -= 1
    graph[s].append(f)
    graph[f].append(s)


def dfs(v: int, num: int) -> None:
    used[v] = 1
    components[v] = num
    for edge in graph[v]:
        if used[edge] == 0:
            dfs(edge, num)


for i in range(n):
    if used[i] == 0:
        count += 1
        dfs(i, count)

print(count)
for i in range(1, count + 1):
    print(components.count(i))
    for j in range(n):
        if components[j] == i:
            print(j + 1, end=" ")
    print()
