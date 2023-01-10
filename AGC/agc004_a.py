abc = list(map(int, input().split()))
abc.sort()
area = 1
for i in range(2):
    area *= abc[i]

if max(abc)%2==0:
    print(0)
else:
    print(area)
