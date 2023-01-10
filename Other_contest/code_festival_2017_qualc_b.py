n = int(input())
a = list(map(int, input().split()))
even_num_count = 0
ans = 0
for num in a:
    if num%2==0:
        even_num_count += 1
#全順列-全部が奇数の数
ans = 3**n - 2**even_num_count
print(ans)
