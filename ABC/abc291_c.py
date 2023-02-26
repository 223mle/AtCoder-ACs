n = int(input())
s = input()

grid = set()
grid.add((0, 0))
now_x = 0
now_y = 0
for i in range(n):
    if s[i]=='R':
        now_x += 1
    elif s[i]=='L':
        now_x -= 1
    elif s[i]=='U':
        now_y += 1
    else:
        now_y -= 1
    if (now_x, now_y) in grid:
        print('Yes')
        exit()
    else:
        grid.add((now_x, now_y))

print('No')
