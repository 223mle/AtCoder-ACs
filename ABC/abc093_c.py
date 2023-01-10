'''
abc = list(map(int, input().split()))

#値の差を考える
max_val = max(abc)
max_val_index = abc.index(max_val)
val_diff = []
for i in range(3):
    if i==max_val_index: continue
    val_diff.append(max_val-abc[i])

#処理
ans = min(val_diff)+(max(val_diff)-min(val_diff))//2
if (val_diff[0]%2)==(val_diff[1]%2):
    print(ans)
else:
    print(ans+2)
'''
#やってることは変わらないが簡潔&賢い
A, B, C = list(map(int, input().split()))

m = max(A, B, C)
diff = [m - A, m - B, m - C]
s = sum(diff)
if s % 2 == 0:
    print(s // 2)
else:
    print((s + 3) // 2)
