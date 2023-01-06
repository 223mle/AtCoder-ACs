n = int(input())
w = [input() for _ in range(n)]
judge = set()
judge.add(w[0])
for i in range(1, len(w)):
    if w[i-1][-1]!=w[i][0] or w[i] in judge:
        print('No')
        exit()
    else:
        judge.add(w[i])
print('Yes')

