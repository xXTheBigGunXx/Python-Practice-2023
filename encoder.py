list = ['a', 'r', 'b', 'u', 'a', 'z', 'a', 'k', 's', 's']
count = 0

for letters in list:
    count +=1

def encoder(list):
    insert_into_first = 0
    inser_letter_1 = 2
    insert_second_into = 1
    insert_into = 2
    total = count // 3
    while total != 0:
        list.insert(insert_into_first, list.pop(inser_letter_1))
        list.insert(insert_into, list.pop(insert_second_into))
        total -=1
        insert_into_first += 3
        inser_letter_1 += 3
        insert_second_into += 3
        insert_into += 3
    print(list)
encoder(list)
