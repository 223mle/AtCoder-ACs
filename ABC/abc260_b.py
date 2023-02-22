n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

math = [(a[i], i+1) for i in range(n)]
english = [(b[i], i+1) for i in range(n)]
both = [(a[i]+b[i], i+1) for i in range(n)]

math = sorted(math, key= lambda x: x[0], reverse=True)
english = sorted(english, key= lambda x: x[0], reverse=True)
both = sorted(both, key= lambda x: x[0], reverse=True)

pass_people = set()

for i in range(x):
    pass_people.add(math[i][1])

pass_eng = 0
eng_idx = 0
while pass_eng<y:
    if english[eng_idx][1] in pass_people:
        eng_idx += 1
        continue
    else:
        pass_people.add(english[eng_idx][1])
        pass_eng += 1
        eng_idx += 1


pass_both = 0
both_idx = 0
while pass_both<z:
    if both[both_idx][1] in pass_people:
        both_idx += 1
        continue
    else:
        pass_people.add(both[both_idx][1])
        pass_both += 1
        both_idx += 1

pass_people = list(pass_people)
pass_people.sort()
print(*pass_people, sep='\n')
