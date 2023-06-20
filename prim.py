import heapq
from typing import Tuple, List

n, m, s = map(int, input().split())
edges = []
mst = []
visited = [False] * n
cost = 0
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))


def prim_algorithm_edge_list(edges: List[Tuple[int, int, int]], vertices: int, start: int) -> List[Tuple[int, int]]:
    global cost, mst, visited
    adj_list = [[] for _ in range(vertices)]
    for src, dest, weight in edges:
        adj_list[src].append((dest, weight))
        adj_list[dest].append((src, weight))
    visited[start] = True
    edge_list = []
    for dest, weight in adj_list[start]:
        heapq.heappush(edge_list, (weight, start, dest))
    while len(edge_list) > 0:
        weight, src, dest = heapq.heappop(edge_list)
        if visited[dest]:
            continue
        mst.append((src, dest))
        visited[dest] = True
        cost += weight
        for new_dest, new_weight in adj_list[dest]:
            if not visited[new_dest]:
                heapq.heappush(edge_list, (new_weight, dest, new_dest))
    return mst


print(prim_algorithm_edge_list(edges, n, s))
print(cost)
