n = int(input())
a = [0]+list(map(int, input().split()))+[0]
dis = [0]
for i in range(n+1):
    dis.append(abs(a[i+1]-a[i]))
sum_dis = sum(dis)
for i in range(n):
    ans = sum_dis
    remove_dis = dis[i+1]+dis[i+2]
    append_dis = abs(a[i+2]-a[i])
    ans = ans-remove_dis+append_dis
    print(ans)
