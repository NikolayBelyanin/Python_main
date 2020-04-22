X = int(input())
Y = int(input())
days = 1
while X < Y:
    X = 0.1 * X + X
    days = days + 1
print(days)
