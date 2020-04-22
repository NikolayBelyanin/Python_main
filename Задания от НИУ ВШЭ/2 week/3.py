a = int(input())
b = int(input())
c = int(input())
max = 0
if a > b and a > c:
    max = a
elif b > c:
    max = b
else:
    max = c
print(max)
