from random import  randint

new_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1','2','3','4','5','6','7','8','9']

total = 0

while total != 1000:
    password = []
    for x in range(1,6):
        random  = randint(0,33)
        choosen = new_list[random]
        password.append(choosen)

    password = ''.join(password)
    password = password.replace(' ', '').replace(',', '')
    print (password)

    file = open("Desktop/projects/password_v1.txt", "a+")
    file.write(password + "\n")
    total += 1 

file.close()
