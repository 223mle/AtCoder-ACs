s = input()
res = ''
for i in range(len(s)):
    res += chr(ord(s[i])-32)
print(res)
