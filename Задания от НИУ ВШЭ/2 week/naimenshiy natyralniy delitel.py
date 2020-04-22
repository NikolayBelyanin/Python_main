N = int(input())
i = 2
mindel = 0
while i <= N:
    if N % i == 0:
        mindel = i
        break
    else:
        i = i + 1
print(mindel)
