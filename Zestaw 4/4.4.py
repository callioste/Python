def fibonacci(n):

    a = 0
    b = 1

    for _ in range(n):
        a, b = b, b + a

    return a


assert fibonacci(1) == 1
assert fibonacci(6) == 8
assert fibonacci(4) == 3

