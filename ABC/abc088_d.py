from queue import Queue
DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

h, w = map(int, input().split())
grid = [input() for _ in range(h)]

que = Queue()
dist = [[-1]*w for _ in range(h)]

que.put((0, 0))
dist[0][0] = 0

while not que.empty():
    x, y = que.get()
    for dx, dy in zip(DX, DY):
        x2 , y2 = x+dx, y+dy

        if x2<0 or x2>=h or y2<0 or y2>=w:
            continue
        if grid[x2][y2]=='#':
            continue
        if dist[x2][y2]!=-1:
            continue

        que.put((x2, y2))
        dist[x2][y2] = dist[x][y] + 1

white = sum(line.count('.') for line in grid)
if dist[h-1][w-1]==-1:
    print(-1)
else:
    # -1はスタート地点(0, 0)を含めるため(最短経路が4でもスタート地点入れるとgrid数は5)
    print(white-dist[h-1][w-1]-1)
