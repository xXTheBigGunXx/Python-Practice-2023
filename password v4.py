from random import randint, choice

file_path = "Desktop/projects/z.txt"
numb_list = ['3', '4', '5', '6', '7', '8', '9']

with open(file_path, "r") as file:
    content = file.read()

words = content.split()
chosen_word = choice(words)

total = 0
while total != 1000:
    def upper_case(chosen_word):
        random_index = randint(0, 4)
        chosen_letter = chosen_word[random_index]
        modified_word = chosen_word[:random_index] + chosen_letter.upper() + chosen_word[random_index + 1:]
        return modified_word, random_index

    chosen_upper, rd_index = upper_case(chosen_word)
    rd_place = (rd_index)

    def add_number(chosen):
        random_index_2 = randint(0,4)
        while rd_place == random_index_2:
            random_index_2 = randint(0,4)
        random_number = choice(numb_list)
        chosen = chosen[:random_index_2] + random_number + chosen[random_index_2 + 1:]
        return chosen

    chosen_upper_number = add_number(chosen_upper)
    print (chosen_upper_number)
    total +=1

    file = open("Desktop/projects/password_v4.txt", "a+")
    file.write(chosen_upper_number + "\n")







