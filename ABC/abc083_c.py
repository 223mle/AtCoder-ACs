x, y = map(int, input().split())
count = 1
for i in range(10**8):
    x *= 2
    if x>y:
        print(count)
        exit()
    count += 1
