n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(1, n+1):
    for j in range(s+1):
        if j-a[i-1]<0:
            if dp[i-1][j]:
                dp[i][j] = True
        else:
            if dp[i-1][j] or dp[i-1][j-a[i-1]]:
                dp[i][j] = True

if dp[n][s]==False:
    print(-1)
    exit()

ans = []
place = s
for i in reversed(range(1, n+1)):
    if dp[i-1][place]: continue
    else:
        place = place - a[i-1]
        ans.append(i)

ans.reverse()
print(len(ans))
print(*ans)
