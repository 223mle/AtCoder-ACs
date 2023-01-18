a, b = map(int, input().split())
ave = b/a
ave_str = list(str(ave))
if len(ave_str)<6:
    ave_str += '0000'

if int(ave_str[5])>=5:
    ave_str[4] = int(ave_str[4])+1
print(*ave_str[:5], sep='')
