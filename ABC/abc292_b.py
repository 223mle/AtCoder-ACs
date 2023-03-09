n, q = map(int, input().split())
player = [0]*(n+1)
for _ in range(q):
    c, x = map(int, input().split())
    if c==1:
        player[x]+=1
    elif c==2:
        player[x]+=2
    else:
        print('Yes' if player[x]>=2 else 'No')
