n = int(input())
h = list(map(int, input().split()))
h_low = [i-1 for i in h]
max_height = h[-1]
judge = True
for i in range(n-1):
    if h_low[i]>h[i+1]:
        judge = False
    if h_low[i]>max_height:
        judge = False
    if not judge:
        print('No')
        exit()
print('Yes')
