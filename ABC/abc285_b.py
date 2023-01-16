n = int(input())
s = input()
for i in range(1, n):
    l = 0
    k = 0
    while l+i<=n-1 or k+i<n:
        if s[k]!=s[k+i]:
            l += 1
            k += 1
        else:
            break
    print(l)
