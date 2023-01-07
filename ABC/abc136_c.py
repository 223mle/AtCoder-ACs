n = int(input())
h = list(map(int, input().split()))
h_low = [i-1 for i in h]
last_height = h[-1]
max_height = 0
judge = True
for i in range(n-1):
    if h_low[i]>h[i+1]:
        judge = False
    if h_low[i]>last_height:
        judge = False
    if max_height-1>h[i]:
        judge = False
    if not judge:
        print('No')
        exit()
    max_height = max(max_height, h[i])
print('Yes')
