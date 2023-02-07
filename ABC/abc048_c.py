n, x = map(int, input().split())
a = list(map(int, input().split()))
res = 0

if a[0]>x:
    res += a[0]-x
    a[0] = x

for i in range(n-1):
    if a[i]+a[i+1]>x:
        res += a[i]+a[i+1]-x
        a[i+1] = x-a[i]
print(res)
