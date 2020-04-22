a = int(input())
if a % 400 == 0 or not(a % 100 == 0) and a % 4 == 0:
    print('Yes')
else:
    print('No')
