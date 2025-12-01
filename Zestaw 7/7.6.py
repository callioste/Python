import itertools
import random

def zero_one_iter():
    return itertools.cycle([0, 1])

def random_direction_iter():
    return (random.choice(["N", "E", "S", "W"]) for _ in iter(int, 1))

def random_weekday_iter():
    return iter(lambda: random.choice(range(7)), -1)


zo = zero_one_iter()
rd = random_direction_iter()
rw = random_weekday_iter()

for i in range(10):
    print(next(zo), end=" ")

print("\n")

for i in range(10):
    print(next(rd), end=" ")

print("\n")

for i in range(10):
    print(next(rw), end=" ")