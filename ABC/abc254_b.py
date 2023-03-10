n = int(input())
A = [[0]*(i+1) for i in range(n)]
A[0][0] = 1
for i in range(1,n):
    for j in range(len(A[i])):
        if i==j or j==0:
            A[i][j] = 1
        else:
            A[i][j] = A[i-1][j-1]+A[i-1][j]
for i in range(n):
    print(*A[i])
