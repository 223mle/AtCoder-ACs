S = [input() for _ in range(3)]
a_index, b_index, c_index = 0, 0, 0
now = 0

def turn(now, index):
    if S[now][index]=='a':
        index += 1
        now = 0
    elif S[now][index]=='b':
        index += 1
        now = 1
    else:
        index += 1
        now = 2
    return now, index

for i in range(100**3):
    if now==0:
        if a_index==len(S[0]):
            print('A')
            exit()
        now, a_index = turn(now, a_index)
    elif now==1:
        if b_index==len(S[1]):
            print('B')
            exit()
        now, b_index = turn(now, b_index)
    else:
        if c_index==len(S[2]):
            print('C')
            exit()
        now, c_index = turn(now, c_index)

