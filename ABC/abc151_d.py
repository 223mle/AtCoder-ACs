from collections import deque

def bfs(g, s, n):
    queue = deque([s])
    d = [0] * n # uからの距離の初期化
    d[s] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i]:
                d[i] = d[v] + 1
                queue.append(i)
    return d

h, w = map(int, input().split())
grid = [input() for _ in range(h)]
DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]
def bfs(sx, sy):
    dist = [[-1]*w for _ in range(h)]
    dist[sy][sx] = 0

    Q = deque()
    Q.append([sy, sx])

    while len(Q)>0:
        y, x = Q.popleft()

        for dy, dx in zip(DY, DX):
            x2 = x+dx
            y2 = y+dy
            if not ((0<=x2<w) and (0<=y2<h)):
                continue
            if grid[y2][x2]=='#':
                continue
            if dist[y2][x2]!=-1:
                continue
            dist[y2][x2] = dist[y][x] + 1
            Q.append([y2, x2])
    max_val = 0

    for i in range(h):
        max_val = max(max_val, max(dist[i]))
    return max_val

val_list = []
for i in range(w):
    for j in range(h):
        if grid[j][i]=='#':
            continue
        val = bfs(i, j)
        val_list.append(val)
print(max(val_list))

