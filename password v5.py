from random import randint, choice
from itertools import repeat
file_path = "Desktop/projects/z.txt"
numb_list = ['3', '4', '5', '6', '7', '8', '9']

with open(file_path, "r") as file:
    content = file.read()

total = 0
while total != 1:
    words = content.split()
    chosen_word = choice(words)
    def upper_case(chosen_word):
        random_index = randint(3, 4)
        chosen_letter = chosen_word[random_index]
        while chosen_letter in ["s", "r", "m", "t"]:
            random_index = randint(3, 4)
            chosen_letter = chosen_word[random_index]
        modified_word = chosen_word[:random_index] + chosen_letter.upper() + chosen_word[random_index + 1:]
        return modified_word, random_index

    chosen_upper, rd_index = upper_case(chosen_word)

    def add_number(chosen):
        random_index_2 = randint(0,2)
        random_number = choice(numb_list)
        while random_number == "6" and chosen[random_index_2] == "g":
            random_number = choice(numb_list)    
        while random_number == "7" and chosen[random_index_2] == "t":
            random_number = choice(numb_list)
        while random_number == "8" and chosen[random_index_2] == "b":
            random_number = choice(numb_list)
        while random_number == "9" and chosen[random_index_2] == "p":
            random_number = choice(numb_list)
        
        chosen = chosen[:random_index_2] + random_number + chosen[random_index_2 + 1:]
        return chosen

    chosen_upper_number = add_number(chosen_upper)
    print (chosen_upper_number)
    total +=1

    #file = open("Desktop/projects/password_v5.txt", "a+")
    #file.write(chosen_upper_number + "\n")