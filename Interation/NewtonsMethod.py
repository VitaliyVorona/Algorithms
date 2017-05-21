
def newtonSqrt(n, iteration_number):
    approx = 0.5 * n
    for i in range(iteration_number):
        better_approx = 0.5 * (approx + n/approx)
        approx = better_approx
    return better_approx

