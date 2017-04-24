
x = []
def sum_digits(n):
    if n < 10:
        # x.append(n)
        return n
    else:
        all_but_last, last = n // 10, n % 10
        print(all_but_last)
        return sum_digits(all_but_last) + last

sum_digits(738)
print(x)