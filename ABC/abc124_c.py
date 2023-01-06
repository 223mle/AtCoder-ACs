s = list(input())
count = 0
for i in range(1, len(s)):
    if s[i-1]==s[i]:
        s[i] = '1' if s[i-1]=='0' else '0'
        count += 1
print(count)
