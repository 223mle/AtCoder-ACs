n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
a = list(set(a))

ans = []
now_count = 0
if a[0]!=0:
    print(0)
    exit()

for i in range(len(a)):
    if a[i]==i:
        ans.append(a[i])
    else:
        break
    if len(a)>i+1 and a[i+1]>=k:
        break

print(len(ans))

