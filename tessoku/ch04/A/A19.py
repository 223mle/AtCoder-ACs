N, W = map(int, input().split())
knapsack = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(W+1):
        w, v = knapsack[i-1]
        if j>=w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]

ans = 0
for i in range(N+1):
    ans = max(max(dp[i]), ans)
print(ans)
print(dp)
