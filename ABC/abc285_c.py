s = input()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
len_alpha = len(alpha)
len_s = len(s)
ans = 0
for i in range(len(s)):
    ans += (alpha.index(s[-i-1])+1)*(26**i)
print(ans)
