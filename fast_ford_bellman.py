# This task from https://acmp.ru/index.asp?main=task&id_task=138
n, m = map(int, input().split())
edges = []
d = [30000] * n
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append([u - 1, v - 1, w])

d[0] = 0
ok = False
while not ok:
    ok = True
    for edge in edges:
        start = edge[0]
        finish = edge[1]
        weight = edge[2]
        if d[start] + weight < d[finish] and d[start] < 30000:
            d[finish] = d[start] + weight
            ok = False

print(*d)
