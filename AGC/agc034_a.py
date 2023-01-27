n, a, b, c, d = map(int, input().split())

s = input()

for i in range(b-1, d-1):
    if s[i]==s[i+1]=='#':
        print('No')
        exit()

for i in range(a-1, c-1):
    if s[i]==s[i+1]=='#':
        print('No')
        exit()

if c>=d:
    if '...' in s[b-2:d+1]:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
print('Yes')
