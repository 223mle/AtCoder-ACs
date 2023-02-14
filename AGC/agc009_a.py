n = int(input())
A = []
B = []
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.reverse()
B.reverse()
for a, b in zip(A, B):
    a += ans
    if a%b != 0:
        ans += b-(a%b)
print(ans)
