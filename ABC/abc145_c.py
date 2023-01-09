def cal_distance(x1, x2, y1, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

from itertools import permutations

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
distance = 0
div = 0
for permutation in permutations(list(range(n))):
    for i in range(len(permutation)-1):
        index_1 = permutation[i]
        index_2 = permutation[i+1]
        x1, y1 = xy[index_1]
        x2, y2 = xy[index_2]
        distance += cal_distance(x1, x2, y1, y2)
    div += 1

print(distance/div)

