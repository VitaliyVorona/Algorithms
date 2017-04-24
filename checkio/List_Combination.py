def list_combination(list1, list2):
    x = []
    for i in list1:
        x.append(i)
        x.append(list2[i])

    return x

print(list_combination([1, 2, 3], [4, 5, 6]))
