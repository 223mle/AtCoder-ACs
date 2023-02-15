n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

min_n = min(a, b, c, d, e)
if n%min_n==0:
    print(5+(n//min_n)-1)
else:
    print(5+(n//min_n))
