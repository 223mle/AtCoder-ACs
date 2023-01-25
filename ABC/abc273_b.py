from decimal import Decimal, ROUND_HALF_UP
x, k = map(int, input().split())

for i in range(k+1):
    x = Decimal(str(x)).quantize(Decimal(f'1e{str(i)}'), rounding=ROUND_HALF_UP)

print(int(x))

'''
for i in range(k):
    x, r = divmod(x, 10)
    x += r>=5
print(x*10**k)

'''
