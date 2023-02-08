n = int(input())
box = set()
for a in range(2, int(n**0.5)+1):
    x = a*a
    while x<=n:
        box.add(x)
        x *= a
print(n-len(box))
