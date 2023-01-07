n = input()
ans = 0

for i in n:
    ans += int(i)
print(max(ans, 9*(len(n)-1) + int(n[0])-1))
