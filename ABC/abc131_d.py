n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]
sorted_AB = sorted(AB, key= lambda x: x[1])
now_time = 0

for i in range(n):
    now_time += sorted_AB[i][0]
    if now_time>sorted_AB[i][1]:
        print('No')
        exit()
print('Yes')
