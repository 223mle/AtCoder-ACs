n, m = map(int, input().split())
judge = [[False]*n for _ in range(n)]
for _ in range(m):
    k, *x = map(int, input().split())
    for i in range(k):
        for j in range(i+1, k):
            judge[x[i]-1][x[j]-1] = True
            judge[x[j]-1][x[i]-1] = True

for i in range(n):
    for j in range(i+1, n):
        if not judge[i][j]:
            print('No')
            exit()
print('Yes')
