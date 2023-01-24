n = int(input())
s = list(map(int, input().split()))
a = s.copy()
for i in range(n-1):
    a[i+1] -= s[i]
print(*a)
