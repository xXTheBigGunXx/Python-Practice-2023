import random

new_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numb_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

total = 0

with open("Desktop/projects/password_v2.txt", "a+") as file:
    while total != 1000:
        password = []
        for _ in range(1,3):
            choose = random.choice(new_list)
            password.append(choose)

        random_numb = random.choice(numb_list)
        password.append(random_numb)

        for _ in range(1,3):
            choose = random.choice(new_list)
            password.append(choose)

        generated_password = ''.join(password)
        file.write(generated_password + "\n")
        print(generated_password)
        total += 1
    
file.close()
