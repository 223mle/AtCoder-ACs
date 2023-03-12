s = input()
res = ''
for i in range(len(s)//2):
    res += s[2*i+1]
    res += s[2*i]
print(res)
