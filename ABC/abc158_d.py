s = list(input())
q = int(input())
reverse = False
head = ''
tail = ''
for i in range(q):
    query = list(input().split())
    if query[0]=='1':
        reverse ^= True
        head, tail = tail, head
    else:
        f = query[1]
        c = query[2]
        if f=='1':
            head += c
        else:
            tail += c

if reverse:
    s = s[::-1]
s = [head[::-1]]+s+[tail]
print(*s, sep='')
