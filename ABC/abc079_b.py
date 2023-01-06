n = int(input())
count = 1
l_i_1 = 1
l_i_2 = 2
if n==1:
    print(1)
    exit()
for i in range(86):
    l = l_i_1+l_i_2
    count += 1
    if count==n:
        print(l)
        exit()
    l_i_1, l_i_2 = l, l_i_1
