k = int(input())
s = input()[:4]
t = input()[:4]

count = [k]*10
for card in s:
    count[int(card)] -= 1
for card in t:
    count[int(card)] -= 1

def cal_score(s):
    count = [0]*10
    for c in s:
        count[int(c)] += 1
    score = 0
    for i in range(1, 10):
        score += i*10**count[i]
    return score

ans = 0

for i in range(1, 10):
    if count[i]==0: continue
    for j in range(1, 10):
        if i==j or count[j]==0: continue
        if cal_score(s+str(i)) > cal_score(t+str(j)):
            ans += count[i]*count[j]

for i in range(1, 10):
    if count[i]<2:
        continue
    if cal_score(s+str(i)) > cal_score(t+str(i)):
        ans += count[i]*(count[i]-1)
n = 9*k-8
print(ans/n/(n-1))
