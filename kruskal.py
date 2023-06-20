n, m = map(int, input().split())
edges = []
res = []
p = [0] * n
cost = 0
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append([u - 1, v - 1, w])


def dsu_find(vertex):
    if vertex == p[vertex]:
        return vertex
    p[vertex] = dsu_find(p[vertex])
    return p[vertex]


def dsu_union(a, b):
    a = dsu_find(a)
    b = dsu_find(b)
    p[b] = a


edges = sorted(edges, key=lambda e: e[2])
for i in range(n):
    p[i] = i

for i in range(m):
    first, second, weight = edges[i][0], edges[i][1], edges[i][2]
    if dsu_find(first) != dsu_find(second):
        cost += weight
        res.append([first, second])
        dsu_union(first, second)


print(cost)
for i in range(len(res)):
    print(*[x + 1 for x in res[i]])
