n, k = map(int, input().split())
s = [input() for _ in range(n)]
new_s = s[:k]
new_s.sort()
for i in range(k):
    print(new_s[i])
