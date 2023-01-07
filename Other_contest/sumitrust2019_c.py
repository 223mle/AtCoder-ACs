x = int(input())
can_buy = x//100
think_money = x%100
count = 0
for i in reversed(range(1, 6)):
    count += think_money//i
    think_money = think_money%i
if count<=can_buy:
    print(1)
else:
    print(0)

"""
n = int(input())
for i in range(10000):
    a = i * 100
    b = i * 105
    if a <= n <= b:
        print(1)
        exit()
print(0)
"""
