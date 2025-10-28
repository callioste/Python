def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(1) == 1
assert fibonacci(6) == 8
assert fibonacci(4) == 3