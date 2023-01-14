s = input()
a_exist = []
for i in range(len(s)):
    if s[i]=='a':
        a_exist.append(i+1)
if len(a_exist)==0:
    print(-1)
else:
    print(max(a_exist))
