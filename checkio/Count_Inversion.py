def count_inversion(sequence):
    counter_of_inversion = 0
    for_counter_outer, index = 0, 0
    for i in sequence:
        increment = 0
        while index + increment < len(sequence):
            if sequence[index] > sequence[index+increment]:
                counter_of_inversion += 1
            increment += 1
        index += 1
    return counter_of_inversion

test = list((10, 1, 2, 5, 3, 4, 7, 6))

x = count_inversion(test)
print(x)