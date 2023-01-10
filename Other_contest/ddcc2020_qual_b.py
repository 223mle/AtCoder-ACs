n = int(input())
a = list(map(int, input().split()))
# 右左の差をなくすのが目的なので、左右の差が一番小さい時が切り時
right = 0
left = sum(a)
ans = 2020202020*2
for i in range(n):
    right += a[i]
    left -= a[i]
    ans = min(ans, abs(right-left))
print(ans)
