n = int(input())
apx = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    apx[i][2] -= apx[i][0]

money = []
for i in range(n):
    if apx[i][2]>0:
        money.append(apx[i][1])
if money==[]:
    print(-1)
else:
    print(min(money))
