from heapq import heappush, heappop
n, m = map(int, input().split())

AtoB = [[] for _ in range(m+1)]
for _ in range(n):
    a, b = map(int, input().split())
    if a>m:
        continue
    AtoB[a].append(b)
res = 0

que = []
for bs in AtoB:
    for b in bs:
        heappush(que, -b)
    #何も入ってない場合、入ってるものから一つ取り出す(後ろからやってるので日にちを越えることはない)
    if que:
        #heapから最小の要素を返す
        res -= heappop(que)
print(res)
