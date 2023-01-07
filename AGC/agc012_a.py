n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
count = 0
for i in range(3*n):
    if i%2==1:
        ans += a[i]
        count += 1
    if count==n:
        break
print(ans)
