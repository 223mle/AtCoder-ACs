n = int(input())
a1 = list(map(int, input().split()))
a2 = [0]+list(map(int, input().split()))
if n==1:
    print(sum(a1)+sum(a2))
    exit()
ans = 0
for i in range(1, n):
    ans = max(ans, sum(a1[1:n-i])+sum(a2[-i-1:]))
    #print(a1[1:n-i], a2[-i-1:])

print(ans+a1[0])
