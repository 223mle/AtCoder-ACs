n = int(input())
b = list(map(int, input().split()))
a = [b[0]]
for i in range(n-1):
    a.append(b[i])
    if a[i+1]<a[i]:
        a[i] = a[i+1]
print(sum(a))
