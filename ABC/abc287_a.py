n = int(input())
For = 0
Against = 0
for i in range(n):
    s = input()
    if s=='For':
        For += 1
    else:
        Against += 1
print('Yes' if For>Against else 'No')
