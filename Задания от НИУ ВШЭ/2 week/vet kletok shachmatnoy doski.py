x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
r1 = ((x1 % 2) + (y1 % 2))
r2 = ((x2 % 2) + (y2 % 2))
if (((r1 + r2) % 2) == 0):
print('YES')
else:
print('NO')
