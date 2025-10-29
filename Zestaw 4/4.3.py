def factorial(n):
    total = 1

    if n == 0:
        return total

    while n > 0:
        total *= n
        n -= 1

    return total

assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(3) == 6

