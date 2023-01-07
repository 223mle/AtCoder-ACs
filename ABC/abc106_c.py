s = input()
k = int(input())

for c in s:
    if c=='1':
        if k==1:
            print(1)
            break
        k -= 1
        continue
    print(c)
    break
