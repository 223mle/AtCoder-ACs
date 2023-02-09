n = int(input())
INF = 10**9
dp = [INF]*(10**5+1)
dp[0], dp[1], dp[6], dp[9] = 0, 1, 1, 1
for i in range(1, n+1):
    p = [i, dp[i-1]+1]
    q = 6
    while q<=i:
        p.append(dp[i-q]+1)
        q*=6
    q = 9
    while q<=i:
        p.append(dp[i-q]+1)
        q*=9
    dp[i] = min(p)
print(dp[n])

'''
N = int(input())
# 1 < N < 100_000
hikidasi = [1]
hikidasi.extend([6**n for n in range(1, 7)])
hikidasi.extend([9**n for n in range(1, 6)])


inf = 2**32
DP = [inf] * (N+1)
DP[0] = 0

for i in range(0, N):
    for j in hikidasi:
        if i+j <= N:
            DP[i+j] = min(DP[i+j], DP[i] + 1)

print(DP[N])
'''
