from random import randint

com_numb = randint(1, 100)

while True:
    users_guess = int(input("Choose a number between 1 and 100! "))
    
    if com_numb == users_guess:
        print("That is the number!")
        break
    elif com_numb > users_guess:
        print("Too low!")
    else:
        print("Too high!")


