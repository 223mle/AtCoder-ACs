import math
n, p = map(int, input().split())
a = list(map(int, input().split()))
odd_num_count = 0
even_num_count = 0
for bis in a:
    if bis%2==0:
        even_num_count += 1
    else:
        odd_num_count += 1

#偶数を選ぶ選ばないでは%2の結果は変わらないため
even_ans = max(1, 2**even_num_count)
odd_ans = 0
for i in range(odd_num_count+1):
    if p==0:
        if i%2==0:
            odd_ans +=  math.comb(odd_num_count, i)
    else:
        if i%2==1:
            odd_ans +=  math.comb(odd_num_count, i)

print(even_ans*odd_ans)
