d, n = map(int, input().split())
count = 0
if d==0:
    if n==100:
        n+=1
    print(n)
else:
    if n==100:
        n+=1
    print(100**d * n)
