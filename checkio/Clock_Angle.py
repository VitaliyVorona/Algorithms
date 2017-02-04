time = input()


def clock_angle(time):
    hours = time[:2]
    minutes = time[3:]
    degree = 0
    hoursFormat = {'12': 0, '13': 1, '14': 2, '15': 3, '16': 4, '17': 5, '18': 6, '19': 7, '20': 8, '21': 9, '22': 10,
                   '23': 11}
    if hours in hoursFormat.keys():
        hours = hoursFormat.get(hours)
    hours_degree = float(hours) * 30.0 + float(minutes) * 0.5
    min_degree = float(minutes) * 6.0
    if min_degree > 180 and min_degree - hours_degree > 180:
        degree = (360 - min_degree) + hours_degree
        print(degree)
    elif hours_degree > 180 and hours_degree - min_degree > 180:
        degree = (360 - hours_degree) + min_degree
        print(degree)
    else:
        degree = hours_degree - min_degree
    return abs(degree)


x = clock_angle(time)
print(x)
