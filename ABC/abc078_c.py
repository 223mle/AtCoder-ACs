n, m = map(int, input().split())
time = 1900*m+(n-m)*100
ans = time*(2**m)
print(ans)
