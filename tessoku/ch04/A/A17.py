n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
INF = 10**9+10
dp = [INF]*(n+1)

dp[1] = 0
dp[2] = a[0]

for i in range(3, n+1):
    dp[i] = min(dp[i-1]+a[i-2], dp[i-2]+b[i-3])

ans = []
place = n
while True:
    ans.append(place)
    if place==1:
        break
    if dp[place-1] + a[place-2] == dp[place]:
        place -= 1
    else:
        place -= 2
ans.reverse()

print(len(ans))
print(*ans)
