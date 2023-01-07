s = input()

tmp = ''
tmp2 = ''
count = 0
for i in s:
    tmp2 += i
    if tmp2 != tmp:
        tmp = tmp2
        tmp2 = ""
        count += 1
print(count)
