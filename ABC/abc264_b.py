r, c = map(int, input().split())
a = min(r, 15-r+1, c, 15-c+1)
if a%2:
    print('black')
else:
    print('white')
