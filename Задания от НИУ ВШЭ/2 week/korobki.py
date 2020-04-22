a, b, c = int(input()), int(input()), int(input())
d, e, f = int(input()), int(input()), int(input())
if a > b:
    (a, b) = (b, a)
if b > c:
    (b, c) = (c, b)
if a > b:
    (a, b) = (b, a)

if d > e:
    (d, e) = (e, d)
if e > f:
    (e, f) = (f, e)
if d > e:
    (d, e) = (e, d)

if (a == d) and (b == e) and (c == f):
    print("Boxes are equal")
elif (a <= d) and (b <= e) and (c <= f):
    print("The first box is smaller than the second one")
elif (a >= d) and (b >= e) and (c >= f):
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
