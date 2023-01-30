n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]
res = 0

for i in range(n):
    dup = False
    for j in range(m):
        if s[i][-3:]==t[j] and not dup:
            res += 1
            dup = True
print(res)
