import bisect
n = int(input())
A = list(map(int, input().split()))
sort_a = sorted(list(set(A)))

b = [0]*n

for i in range(n):
    rank = bisect.bisect_left(sort_a, A[i])
    b[i] = rank + 1

print(*b)
