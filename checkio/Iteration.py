def sumTo(a_bound):
    the_sum = 0
    for i in range(0, a_bound + 1):
        the_sum += i
    return the_sum


def sumToWhile(a_bound):
    the_sum, inc = 0, 0
    while inc <= a_bound:
        the_sum += inc
        inc += 1
    return the_sum

print(sumTo(5))
print(sumToWhile(5))