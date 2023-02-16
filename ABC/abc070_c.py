n = int(input())

import functools, math
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*integers):
    return functools.reduce(my_lcm_base, integers)

t = [int(input()) for _ in range(n)]
print(my_lcm(*t))
