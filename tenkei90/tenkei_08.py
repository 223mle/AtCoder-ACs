n = int(input())
s = input()

mod = 10**9+7
t = 'atcoder'

dp = [[0]*(len(t)+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(len(t)+1):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod

        if j<len(t) and s[i]==t[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod

print(dp[n][len(t)])
print(dp)
