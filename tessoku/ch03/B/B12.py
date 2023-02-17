n = int(input())

def check_large(x, n):
    if x**3+x>n:
        return True
    else:
        return False

right = 10**2
left = 0.0

while right-left>0.001:
    middle = (right+left)/2
    if check_large(middle, n):
        right = middle
    else:
        left = middle
print(right)
