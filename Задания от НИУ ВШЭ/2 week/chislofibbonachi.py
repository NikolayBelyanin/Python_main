fib1 = fib2 = 1 
n = int(input())
while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
print(fib2)
