n = int(input())
a = list(map(int, input().split()))
G = [[] for _ in range(n+1)]
for i in range(n):
    G[i+1].append(a[i])
count = 0
for i in range(n):
    if G[a[i]]==[i+1]:
        count += 1
print(count//2)

