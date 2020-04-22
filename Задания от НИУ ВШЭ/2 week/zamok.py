a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if d > e:
    d, e = e, d
if a <= d and b <= e:
    print('YES')
else:
    print('NO')
