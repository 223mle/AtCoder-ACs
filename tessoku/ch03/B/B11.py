import bisect
n = int(input())
A = list(map(int, input().split()))
A.sort()
q = int(input())


for i in range(q):
    x = int(input())
    print(bisect.bisect_left(A, x))
