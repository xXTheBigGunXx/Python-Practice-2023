word = input("what is the word that you want to encode? ")
new_list  = []
count = 0

for letter in word:
    count += 1 
    new_list.append(letter)

def shuffler(new_list):
    first_index = 0
    second_index = 1
    insert_index = 2
    times_repeat = count // 3
    while times_repeat != 0:
        new_list.insert(insert_index, new_list.pop(first_index))
        new_list.insert(first_index, new_list.pop(second_index))
        first_index += 3
        second_index += 3
        insert_index += 3
        times_repeat -=1
    print (new_list)

shuffler(new_list)
