n = int(input())
h = list(map(int, input().split()))

INF = 10**9+10
dp = [INF]*(n+1)

dp[1] = 0
dp[2] = abs(h[1]-h[0])

for i in range(3, n+1):
    dp[i] = min(dp[i-1]+abs(h[i-1]-h[i-2]), dp[i-2]+abs(h[i-1]-h[i-3]))

place = n
ans = []

while True:
    ans.append(place)
    if place==1:
        break
    if dp[place]==dp[place-1]+abs(h[place-1]-h[place-2]):
        place -= 1
    else:
        place -= 2

ans.reverse()
print(len(ans))
print(*ans)
