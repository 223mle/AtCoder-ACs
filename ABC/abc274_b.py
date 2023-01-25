h, w = map(int, input().split())
grid = [input() for _ in range(h)]
grid_t = [''.join(s) for s in zip(*grid)] # 行列の転置
for i in range(w):
    print(grid_t[i].count('#'))
