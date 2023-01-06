w = input()
from collections import defaultdict
dic = defaultdict(int)
for i in range(len(w)):
    dic[w[i]] += 1

for val in dic.values():
    if val%2!=0:
        print('No')
        exit()
print('Yes')
