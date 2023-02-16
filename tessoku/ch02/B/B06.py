n = int(input())
A = list(map(int, input().split()))
psum = [0]*(n+1)
for i in range(1, n+1):
    psum[i] = psum[i-1]+A[i-1]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    if (psum[r]-psum[l-1]) > (r-l+1)-(psum[r]-psum[l-1]):
        print('win')
    elif (psum[r]-psum[l-1])==(r-l+1)-(psum[r]-psum[l-1]):
        print('draw')
    else:
        print('lose')
