n = int(input())
a = list(map(int, input().split()))
even_num = []
for num in a:
    if num%2==0:
        even_num.append(num)
count = 0
while True:
    judge = False
    for i in range(len(even_num)):
        if even_num[i]%2==0:
            even_num[i] = even_num[i]//2
            count += 1
            judge = True
    if not judge:
        break
print(count)
'''
やってることは同じだけどこっちの方が綺麗
N = int(input())
*A, = map(int, input().split())
ans = 0
for a in A:
    while a % 2 == 0:
        a //= 2
        ans += 1
print(ans)
'''
