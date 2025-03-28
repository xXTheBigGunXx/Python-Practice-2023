from forpro import median

new_list_1 = []
new_list = [63, 100, 80, 67, 86, 73, 97, 96, 87, 52]
new_list.sort()

middle = median(new_list)
print("Middle median:", middle)

list_new = []

for number in new_list:
    if number < middle:
        new_list_1.append(number)
    else:
        list_new.append(number)

print (new_list_1)
print (list_new)
first = median(new_list_1)
print (first)
second = median(list_new)
print (second)