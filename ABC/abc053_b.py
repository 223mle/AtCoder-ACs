s = input()
start_a = 0
end_z = 0
for i in range(len(s)):
    if s[i]=='A':
        start_a = i
        break
for i in reversed(range(len(s))):
    if s[i]=='Z':
        end_z = i
        break
print(end_z-start_a+1)
