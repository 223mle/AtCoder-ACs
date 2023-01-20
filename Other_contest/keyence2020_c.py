n, k, s = map(int, input().split())
ans_array =[]
if s>=10**9:
    append_num = 1
else:
    append_num = s+1

for i in range(k):
    ans_array.append(s)
for i in range(k, n):
    ans_array.append(append_num)
print(*ans_array, sep=' ')
