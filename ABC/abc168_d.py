from collections import deque

def bfs(graph, N, start):
    visited = [0] * N
    visited[start] = 1
    que = deque([start])
    while que:
        node = que.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = node + 1
                que.append(n)
    return visited

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)
print(bfs(G, n, 0))
visited = bfs(G, n, 0)[1:]

if all(visited):
    print('Yes')
    print(*visited, sep='\n')
else:
    print('No')
