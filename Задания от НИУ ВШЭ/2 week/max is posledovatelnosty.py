now = int(input())
max = now
while now != 0:
    now = int(input())
    if now > max and now != 0:
        max = now
print(max)
