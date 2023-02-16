t = int(input())
n = int(input())
psum_prep = [0]*(t+2)
psum = [0]*(t+2)

for i in range(n):
    l, r = map(int, input().split())
    psum_prep[l] += 1
    psum_prep[r] -= 1

psum[0] = psum_prep[0]
for i in range(1, t+2):
    psum[i] = psum[i-1] + psum_prep[i]

for i in range(t):
    print(psum[i])
