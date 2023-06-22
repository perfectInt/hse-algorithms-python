n, m = map(int, input().split())
edges = []
mst = []
parent = [i for i in range(n)]
rank = [0 for i in range(n)]
cheapest = [-1 for i in range(n)]
cost = 0
num_trees = n
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append([u - 1, v - 1, w])


def find(vertex: int):
    if parent[vertex] == vertex:
        return vertex
    return find(parent[vertex])


def union(x: int, y: int):
    x_root = find(x)
    y_root = find(y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x


while num_trees > 1:
    for node in range(n):
        cheapest[node] = -1

    for i in range(len(edges)):
        u, v, w = edges[i]
        set1 = find(u)
        set2 = find(v)

        if set1 != set2:
            if cheapest[set1] == -1 or cheapest[set1][2] > w:
                cheapest[set1] = [u, v, w]
            if cheapest[set2] == -1 or cheapest[set2][2] > w:
                cheapest[set2] = [u, v, w]

    for i in range(n):
        if cheapest[i] != -1:
            u, v, w = cheapest[i]
            set1 = find(u)
            set2 = find(v)

            if set1 != set2:
                cost += w
                union(set1, set2)
                num_trees -= 1
                mst.append([u, v])


print(cost)
print(*mst)
