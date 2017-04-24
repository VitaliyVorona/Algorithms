from math import sqrt


def findHypot(cat_a, cat_b):
    hypot = sqrt((cat_a * cat_a) + (cat_b * cat_b))
    return hypot


print(findHypot(5, 3))


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_odd(x):
    if is_even(x):
        return False
    else:
        return True

print(is_odd(12))