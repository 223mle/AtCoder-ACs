h, w= map(int, input().split())
S = [input() for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if S[i][j]=='#':
            ans += 1
print(ans)
