n, m = map(int, input().split())

mod = 1000000007
able = [True]*(n+1)
for _ in range(m):
    able[int(input())] = False

dp = [0]*(n+1)
dp[0] = 1
for i in range(1, n+1):
    if not able[i]:
        continue
    dp[i] += dp[i-1]
    if i-2>=0:
        dp[i] += dp[i-2]
    dp[i] %= mod
print(dp[-1])
