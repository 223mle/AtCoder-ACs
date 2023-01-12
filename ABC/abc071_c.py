from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
a_dic = defaultdict(int)
for i in range(n):
    a_dic[a[i]] += 1
has_two_side = []
for k, v in a_dic.items():
    if v>=2:
        has_two_side.append((k, v))
if len(has_two_side)<2:
    print(0)
    exit()
has_two_side.sort(reverse=True)
if has_two_side[0][1]>=4:
    print(has_two_side[0][0]**2)
else:
    print(has_two_side[0][0]*has_two_side[1][0])

