x, y = map(int, input().split())

ans = 0

if (x>0 and y>0 and x>y) or (x<0 and y<0 and x>y):
    ans += 1
    x *= -1

ans += abs(abs(x)-abs(y))
x += abs(abs(x)-abs(y))

if x!=y:
    ans += 1
print(ans)
