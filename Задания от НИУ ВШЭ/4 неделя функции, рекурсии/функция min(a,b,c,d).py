def minimum(a, b, c, d):
    x1 = min(a, b)
    x2 = min(c, d)
    return min(x1, x2)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(minimum(a, b, c, d))
