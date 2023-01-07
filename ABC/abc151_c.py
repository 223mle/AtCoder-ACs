n, m = map(int, input().split())
ps = [input().split() for _ in range(m)]
wa = 0
ac = set()
already = set()
for i in range(m):
    if ps[i][1]=="AC":
        ac.add(ps[i][0])
for i in range(m):
    if ps[i][0] in already: continue
    if ps[i][1]=='WA':
        if ps[i][0] in ac:
            wa += 1
    if ps[i][1]=='AC':
        already.add(ps[i][0])
print(len(ac), wa)
