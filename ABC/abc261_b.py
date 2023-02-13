n = int(input())
a = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j]=='W' and a[j][i]=='L': continue
        if a[i][j]=='L' and a[j][i]=='W': continue
        if a[i][j]=='D' and a[j][i]=='D': continue
        if a[i][j]=='-': continue
        print('incorrect')
        exit()
print('correct')



