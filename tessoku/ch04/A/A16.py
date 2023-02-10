n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
INF = 10**9
dp = [INF]*(n+100)
dp[0] = 0

for i in range(1, n):
    dp[i] = min(dp[i-1]+a[i-1], dp[i])
    if i-2>=0:
        dp[i] = min(dp[i-2]+b[i-2], dp[i])



print(dp[n-1])
