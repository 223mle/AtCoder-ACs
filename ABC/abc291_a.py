s = input()
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(s)):
    if s[i] in abc:
        print(i+1)
