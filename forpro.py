from math import floor as fl
def median(x):
    length = len(x)
    x.sort()

    if length % 2 == 0:
        middle = fl(length / 2)
        down_num = x[middle - 1]
        up_num = x[middle]
        total = (down_num + up_num) / 2
    else:
        middle =(length // 2)
        total = x[middle]
    return total


def split_list(x, y, z):
    for number in x:
        if number < median(x):
            y.append(number)
        else:
            z.append(number)
    return y, z

def new(x, y, z):
    for number, frequency in zip(x, y):
        while frequency != 0:
            z.append(number)
            frequency -= 1

    return z