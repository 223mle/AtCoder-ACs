"""n = int(input())
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


divisor = make_divisors(n)
min_ans = 10**12
if len(divisor)%2==1:
    print(divisor[len(divisor)//2]*2 - 2)
    exit()
for i in range(len(divisor)//2):
    min_ans = min(min_ans, divisor[i]+divisor[-i-1])
print(min_ans-2)

"""

N = int(input())
ans = 10**12
for i in range(1, int(N**(1/2)+1)):
    if N % i == 0:
        ans = min(ans, i + N//i - 2)
print(ans)
