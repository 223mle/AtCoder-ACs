n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
ans = n*10**9
p = 0
for i in range(n-1):
    p += a[i]
    sum_a -= a[i]
    ans = min(ans, abs(p-sum_a))
print(ans)
