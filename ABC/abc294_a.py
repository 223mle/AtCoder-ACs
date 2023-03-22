n = int(input())
a = list(map(int, input().split()))
ans = []
for num in a:
    if num%2==0:
        ans.append(num)
print(*ans)
