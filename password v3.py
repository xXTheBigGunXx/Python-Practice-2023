from random import shuffle, choice, randint

new_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'p', 'q', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numb_list =  ['1','2','3','4','5','6','7','8','9']

shuffle(new_list)
shuffle(numb_list)

for letter in range(len(new_list)):
    new_list[letter] = new_list[letter].upper()

total = 0

while total != 1000:
    password = []
    length = 0
    while length < 3:
        rd = choice(new_list)
        password.append(rd)
        length += 1
    shuffle(password)
    while length <5:
        position = randint(1,5)
        random_number = choice(numb_list)
        password.insert(position, random_number)
        length += 1
    new_password =''.join(password)
    print(new_password)
    total +=1

    file = open("Desktop/projects/password_v3", "a")
    file.write(new_password + "\n")

file.close()