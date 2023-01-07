n = int(input())
SP = [list(input().split()) for i in range(n)]
for i in range(n):
    SP[i].append(i)
sorted_sp = sorted(SP, key= lambda x: (x[0], -int(x[1])))
for i in range(n):
    print(sorted_sp[i][2]+1)

"""
N = int(input())
a = []
for i in range(N):
    N, K = input().split()
    K = int(K)
    a.append([N, -K, i+1])
a.sort()
for a_ in a:
    print(a_[2])

"""
