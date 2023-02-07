n = int(input())
v = list(map(int, input().split()))
v.sort()
now_val = v[0]
for i in range(1, n):
    now_val = (now_val+v[i])/2
print(now_val)
