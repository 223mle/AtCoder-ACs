n = int(input())
p = list(map(int, input().split()))
count = 1
i = n-2
while p[i]!=1:
    count += 1
    i = p[i]-2
print(count)

