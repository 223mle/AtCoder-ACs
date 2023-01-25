n, m = map(int, input().split())
G = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in range(1, n+1):
    sorted_downtown = G[i]
    sorted_downtown.sort()
    print(len(sorted_downtown), *sorted_downtown)
