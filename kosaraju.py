# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=56&id_problem=1047 (Задача не сделана полностью если что)
n, m = map(int, input().split())
g = [[] for i in range(n)]
h = [[] for j in range(n)]
used = [0] * n
comps = [0] * n
cnt = 0
order = []
for i in range(m):
    s, f = map(int, input().split())
    g[s - 1].append(f - 1)
    h[f - 1].append(s - 1)


def dfs1(v: int) -> None:
    global used, order
    used[v] = 1
    for to in h[v]:
        if used[to] == 0:
            dfs1(to)
    order.append(v)


def dfs2(v: int, c: int) -> None:
    global comps
    comps[v] = c
    for to in g[v]:
        if comps[to] == 0:
            dfs2(to, c)


for i in range(n):
    if used[i] == 0:
        dfs1(i)

for i in range(len(order) - 1, 0, -1):
    if comps[order[i]] == 0:
        cnt += 1
        dfs2(order[i], cnt)

print(cnt)
print(*comps)
