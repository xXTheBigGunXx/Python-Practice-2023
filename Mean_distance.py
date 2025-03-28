list = [50, 38, 35, 49, 80, 53, 62, 50, 29]
lenght = len(list)
mean_num = sum(list)/lenght
print ('{:.3f}'.format(mean_num))
total = 0
for number in list:
        dif = float(number - mean_num)
        dif = float(('{:.2f}'.format(dif)))
        distance = dif ** 2
        distance = float(('{:.2f}'.format(distance)))
        total = total + distance
        list.remove(number)
print ((total))
