t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for num in a:
        if num%2==1:
            count += 1
    print(count)
