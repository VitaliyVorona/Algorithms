def checkio(number):
    # number = [i*i for i in list(number)]
    lst = [int(i) for i in str(number)]
    n = 1
    for i in lst:
        if i != 0:
            n = n * i
    return n


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
