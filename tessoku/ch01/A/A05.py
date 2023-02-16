n, k = map(int, input().split())
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        diff = k-i-j
        if diff>0 and diff<=n:
            ans += 1
print(ans)
