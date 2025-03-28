X = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
lenght = len(X)

def mean(x):
    s = sum(X)
    print(s/lenght)
    return mean(x)

def median(x):
    if lenght % 2 == 0:
        middle = int(lenght / 2)
        down_num = X[middle - 1]
        up_num = X[middle]
        print  ((down_num + up_num) / 2)
    else:
        middle = int(lenght / 2)
        print (X[middle])
median(X)

def sort(x):
    new_list = []
    new_ss = x
    while new_ss != []:
        minimum = min(new_ss)
        new_list.append(minimum)
        new_ss.remove(minimum)
    return new_list

list_new = sort(X)

def count_dupes(x):
    counts = {}
    for num in list_new:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num, count in counts.items():
        print(num, "s are -", count)

count_dupes(list_new)