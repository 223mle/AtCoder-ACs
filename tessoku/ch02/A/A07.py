d = int(input())
n = int(input())
psum_prep = [0]*(d+2)

for _ in range(n):
    l, r = map(int, input().split())
    psum_prep[l] += 1
    psum_prep[r+1] -= 1

psum = [0]*(d+2)
for i in range(1, len(psum_prep)):
    psum[i] = psum[i-1] + psum_prep[i]

for i in range(1, d+1):
    print(psum[i])
