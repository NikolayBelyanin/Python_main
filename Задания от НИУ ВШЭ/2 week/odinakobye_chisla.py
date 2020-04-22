a = int(input())
b = int(input())
c = int(input())
if a - b == 0 and b - c == 0:
    print(3)
elif a - b == 0 or b - c == 0 or a - c == 0:
    print(2)
else:
    print(0)
