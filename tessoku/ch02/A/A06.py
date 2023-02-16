n, q = map(int, input().split())
A = list(map(int, input().split()))
psum = [0]*(n+1)

for i in range(1, n+1):
    psum[i] = psum[i-1]+A[i-1]

for i in range(q):
    l, r = map(int, input().split())
    print(psum[r]-psum[l-1])
