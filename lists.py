def sorting_by_index(new_list, index):
    for i in range(len(new_list)):
        for j in range(i + 1, len(new_list)):
            first_digit = int(str(new_list[i])[index])
            second_digit = int(str(new_list[j])[index])

            if first_digit < second_digit:
                new_list[i], new_list[j] = new_list[j], new_list[i]

new_list = [337, 477, 879, 164, 941, 444, 214, 914, 985, 640]

for digit in range(-1, -4, -1):
    sorting_by_index(new_list, digit)
    print(new_list)
