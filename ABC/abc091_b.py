from collections import defaultdict
n = int(input())
card = defaultdict(int)
for _ in range(n):
    card[input()] += 1


m = int(input())
for _ in range(m):
    card[input()] -= 1

print(max(0, max(card.values())))
