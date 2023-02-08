s = int(input())
mod = 10**9+7

dp = [0]*(s+1)
dp[0] = 1
"""
for i in range(3, s+1):
    val = 0
    for j in range(3, i+1):
        val += dp[i-j]
        val %= mod
    dp[i] = val

ans = dp[s]%mod
print(ans)
"""

for v in range(1, s+1):
    for d in range(v-2):
        dp[v] += dp[d]
        dp[v] %= mod
print(dp[s])
