l, r = map(int, input().split())
ans = 10**10
#l+2019よりもrが大きくても、modなので意味ない
for i in range(l, min(l+2019, r)):
    for j in range(l+1, min(l+2019, r)+1):
        ans = min(ans, i*j%2019)
print(ans)
