s = input()
S_false = (('N' in s) and ('S' not in s))
N_false = (('N' not in s) and ('S' in s))
W_false = (('E' in s) and ('W' not in s))
E_false = (('E' not in s) and ('W' in s))
if S_false or N_false or W_false or E_false:
    print('No')
else:
    print('Yes')

"""
S=input()
n,w,e,s='N' in S, 'W' in S, 'E' in S, 'S' in S
print('Yes' if (n==s and e==w) else 'No')
"""
