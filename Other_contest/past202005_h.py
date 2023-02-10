n, l = map(int, input().split())
x = set(map(int, input().split()))
t = list(map(int, input().split()))
INF = 10**9
dp = [INF]*(l+100)
dp[0] = 0
for i in range(l):
    if i+1 in x:
        dp[i+1] = min(dp[i]+t[2]+t[0], dp[i+1])
    else:
        dp[i+1] = min(dp[i]+t[0], dp[i+1])
    if i+2 in x:
        dp[i+2] = min(dp[i]+t[0]+t[1]+t[2], dp[i+2])
    else:
        dp[i+2] = min(dp[i]+t[0]+t[1], dp[i+2])
    if i+4 in x:
        dp[i+4] = min(dp[i]+t[0]+3*t[1]+t[2], dp[i+4])
    else:
        dp[i+4] = min(dp[i]+t[0]+t[1]*3, dp[i+4])

# ジャンプで通り過ぎる場合
if l-1 >= 0:
    dp[l] = min(dp[l], dp[l-1] + t[0]//2 + t[1] // 2)
if l-2 >= 0:
    dp[l] = min(dp[l], dp[l-2] + t[0]//2 + t[1] + t[1] // 2)
if l-3>=0:
    dp[l] = min(dp[l], dp[l-3] + t[0]//2 + t[1]*2 + t[1] // 2)

print(dp[l])
