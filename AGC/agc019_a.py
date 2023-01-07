qhsb = list(map(int, input().split()))
n = int(input())
money = 0
sort_qhsb = [(qhsb[0]*8, 0.25, 0), (qhsb[1]*4, 0.5, 1), (qhsb[2]*2, 1, 2), (qhsb[3], 2, 3)]
sort_qhsb.sort()

for i in range(4):
    money += qhsb[sort_qhsb[i][2]] * int(n//sort_qhsb[i][1])
    n = n%sort_qhsb[i][1]

print(money)


"""
自分のコード汚すぎる
頭柔らかくしたら下のコードのようになる
q, h, s, d = map(int,input().split())
n = int(input())
h = min(h, 2*q)
s = min(s, 2*h)
d = min(d, 2*s)
print(d*(n//2) + s*(n%2))
"""
