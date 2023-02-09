n, m = map(int, input().split())
g = [[False] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u][v] = True
    g[v][u] = True
count = 0
for a in range(n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            if g[a][b] and g[b][c] and g[c][a]:
                count += 1
print(count)
