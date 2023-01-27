n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]
t.sort()
bus_num = 1
ride_bus = 1
most_wait_people = t[0]
for i in range(1, n):
    if t[i]>most_wait_people+k or ride_bus==c:
        bus_num += 1
        most_wait_people = t[i]
        ride_bus = 1
    else:
        ride_bus += 1

print(bus_num)
