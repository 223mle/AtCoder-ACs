n, k = map(int, input().split())
a = list(map(int, input().split()))

def check(x, N, K, A):
    res = 0
    for i in range(N):
        res += x//A[i]
    if res>=K:
        return True
    else:
        return False

left = 0
right = 10**9

while right-left>1:
    mid = (right+left)//2
    if check(mid, n, k, a):
        right = mid
    else:
        left = mid
print(right)

