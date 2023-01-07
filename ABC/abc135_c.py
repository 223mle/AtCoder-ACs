n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
first_b = sum(b)
for i in range(n):
    b[i] -= min(a[i], b[i])
    rem_b = b[i]
    b[i] -= min(a[i+1], b[i])
    a[i+1] -= min(a[i+1], rem_b)

print(first_b-sum(b))


