n = int(input())
p = list(map(int, input().split()))
count = 0
neibor = False
for i in range(n):
    if p[i]==(i+1):
        if neibor:
            neibor = False
        else:
            count += 1
            neibor = True
    else:
        if neibor:
            neibor = False
print(count)
