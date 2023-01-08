"""
n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
graph = set()
count = 0
for i in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(G)
"""
from typing import List, Tuple

def dfs(G: List[List[int]], v: int, seen: List[bool]):
    seen[v] = True
    for e in G[v]:
        if not seen[e]:
            dfs(G, e, seen)

def count_connected_components(n: int, m: int, edges: List[Tuple[int, int]]) -> int:
    G = [[] for _ in range(n+1)]
    for a, b in edges:
        G[a].append(b)
        G[b].append(a)

    seen = [False] * (n+1)
    cnt = 0
    for i in range(n+1):
        if not seen[i]:
            dfs(G, i, seen)
            cnt += 1
    return cnt

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(count_connected_components(n, m, edges)-1)
