def sum():
    a = int(input())
    if a != 0:
        return a + sum()
    return 0
print(sum())
