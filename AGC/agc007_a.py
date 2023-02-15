h, w = map(int, input().split())
A = [input() for _ in range(h)]

sharp_count = 0

for i in range(h):
    sharp_count += A[i].count('#')

print('Possible' if sharp_count==(h+w-1) else 'Impossible')
