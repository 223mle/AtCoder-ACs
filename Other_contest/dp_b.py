n, k = map(int, input().split())
h = list(map(int, input().split()))
INF = 10**9
dp = [INF]*(n)
dp[0] = 0
for i in range(1, n):
    for j in range(1, min(k, i)+1):
        dp[i] = min(dp[i], dp[i-j]+abs(h[i-j]-h[i]))
print(dp[-1])

