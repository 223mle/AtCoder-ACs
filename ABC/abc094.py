n = int(input())
x = list(map(int, input().split()))
sorted_x = sorted(x)
median_right = sorted_x[n//2]
median_left = sorted_x[(n//2)-1]
for i in range(n):
    if x[i]<=median_left:
        print(median_right)
    else:
        print(median_left)
