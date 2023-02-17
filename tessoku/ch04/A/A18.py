n, s = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(1, n+1):
    for j in range(s+1):
        if j-A[i-1]<0:
            if dp[i-1][j]:
                dp[i][j] = True
        else:
            if dp[i-1][j] or dp[i-1][j-A[i-1]]:
                dp[i][j] = True
print('Yes' if dp[n][s] else 'No')
