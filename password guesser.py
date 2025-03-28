import time

list_all = ("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789")
List=  []
for letters in list_all:
    List.append(letters)
print (List)

start_time=time.time()
password = ["qqq99"]

def solver(list,password):
    tries = 0
    first_index = 0
    second_index = 0
    third_index = 0
    four_index = 0
    five_index = 0
    new_list = []
    solved = False
    while not solved:
        if five_index == 61:
            four_index += 1
            five_index = 0
        if four_index == 61:
            third_index += 1
            four_index = 0
        if third_index == 61:
            second_index +=1
            third_index = 0
        if second_index == 61:
            first_index +=1
            second_index = 0
        if first_index == 61:
            first_index = 60
        new_list.append(list[first_index] + list[second_index] + list[third_index] + list[four_index] + list[five_index])
        if new_list != password:
            print (new_list)
            new_list.clear()
        else:
            print (new_list , "There", tries)
            solved = True
        five_index +=1
        tries +=1

solver(List,password)
end_time = time.time()
print (end_time - start_time)