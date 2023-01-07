n, a, b = map(int, input().split())

if (b-a)%2==0:
    print((b-a)//2)
else:
    print(min((a+b-1)//2, ((n-a)+(n-b+1))//2))
