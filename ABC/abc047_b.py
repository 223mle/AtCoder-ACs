w, h, n = map(int, input().split())
X = [True]*(w)
Y = [True]*(h)

for i in range(n):
    x, y, a = map(int, input().split())
    if a==1:
        for j in range(x):
            X[j] = False
    if a==2:
        for j in range(w-x):
            X[-j-1] = False
    if a==3:
        for j in range(y):
            Y[j] = False
    if a==4:
        for j in range(h-y):
            Y[-j-1] = False

print(X.count(True)*Y.count(True))


