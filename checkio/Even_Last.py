def even_last(array):
    if len(array) == 0:
        return 0
    last_val = array[len(array) - 1]
    x = sum(array[::2])

    return x * last_val
