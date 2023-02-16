n = int(input())
s = [list(input()) for _ in range(n)]
use_s = sorted(s[0])
ans = ''
used_s = set()
for i in range(len(use_s)):
    now_s = use_s[i]
    if now_s in used_s:
        continue
    min_count = 60
    used_s.add(now_s)
    for j in range(n):
        min_count = min(min_count, s[j].count(now_s))
    ans += now_s*min_count
print(ans)
