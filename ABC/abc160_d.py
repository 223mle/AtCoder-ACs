n, x, y = map(int, input().split())
x, y = x-1, y-1

def dist(a, b):
    return min(abs(b-a), abs(x-a)+1+abs(b-y), abs(y-a)+1+abs(b-x))

ans = [0]*n
for i in range(n):
    for j in range(i):
        ans[dist(i, j)] += 1

for a in ans[1:]:
    print(a)
