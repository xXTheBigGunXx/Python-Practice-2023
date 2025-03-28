def solver(list, password):
    first_index = -1
    second_index = 0
    third_index = 0
    four_index = 0
    five_index = 0
    new_list = []
    solved = False
    while not solved and first_index < 4:
        new_list.append(list[first_index] + list[second_index] + list[third_index] + list[four_index] + list[five_index])
        if new_list != password:
            print(new_list)
            new_list = []
        else:
            print(new_list, "There", first_index, second_index, third_index, four_index, five_index)
            solved = True

        if five_index == 4:
            four_index += 1
            five_index = 0
        elif four_index == 4:
            third_index += 1
            four_index = 0
        elif third_index == 4:
            second_index += 1
            third_index = 0
        elif second_index == 4:
            first_index += 1
            second_index = 0
        elif first_index == 3:
            first_index = 2
            second_index = 3
            third_index = 4
        else:
            five_index += 1

list = ["a", "b", "c", "d", "e"]
password = ["eeeee"]
solver(list, password)
