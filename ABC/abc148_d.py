n = int(input())
a = list(map(int, input().split()))
ans = 0
now_number = 1
for i in range(n):
    if a[i]!=now_number:
        ans += 1
    else:
        now_number+=1
if now_number==1:
    print(-1)
else:
    print(ans)

