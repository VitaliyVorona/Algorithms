def most_numbers(*args):
    args = sorted(args)
    min_value = float(args[0])
    print('min value', min_value)
    max_value = float(args[len(args) - 1])
    print('max value', max_value)
    value_btw_min_max = 0
    kostyl = round(max_value % 1, 2)

    while min_value <= max_value:
        print(min_value, "--", max_value)
        if value_btw_min_max == 0:
            fract_min_val = abs(min_value)
            value_btw_min_max += round(fract_min_val % 1, 2)
            print(value_btw_min_max)
        else:
            value_btw_min_max += 1
            print(value_btw_min_max)
            min_value += 1

    print('ko', kostyl)
    return (value_btw_min_max - 1) + kostyl


x = most_numbers(10.2, -2.2, 0, 1.1, 0.5)
print(x)
