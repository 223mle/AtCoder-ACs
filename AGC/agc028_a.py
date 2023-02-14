from fractions import gcd

def solve(n, m, s, t):
    g = gcd(n, m)
    ng = n // g
    mg = m // g

    for h in range(g):
        if s[ng * h] != t[mg * h]:
            return -1
    return ng * mg * g


n, m = list(map(int, input().split()))
s = input()
t = input()
print(solve(n, m, s, t))
