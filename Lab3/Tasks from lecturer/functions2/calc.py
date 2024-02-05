def calculate_running_average(*args):
    lst = []
    summa = 0
    index = 0
    for arg in args:
        summa += arg
        index += 1
        lst.append(summa/index)

    return lst


print(calculate_running_average(1, 2, 3, 4, 5, 6, 7, 10, 16, 45))



