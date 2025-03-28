from random import randint

def main():
    game_over = False;
    dict = {1:'rock', 2:'paper',3:'scissors'}

    while(game_over == False):
        item = randint(1,3)
        user_input = input("What is your choice - ").lower()

        if type(user_input) is str and user_input in dict.values():
            print(f"Your choice is {user_input}.")
            print(f"Computers choise is {dict[item]}.")

            conclusion = state(dict[item], user_input)
            print(f"State of a game is a - {conclusion}!")

        else:
            print("Your input is invalid!")
        
        try_again = input("Do you wanna try again? ")
        if try_again.lower() == 'no' or try_again.lower() == 'nah':
            game_over = True;
        print()
    print("GOOD GAME!!!")

def state(item, user_input):
    if item == user_input:
        return 'Draw'
    if user_input == 'rock':
        if item == 'scissors': return 'Win'
        else: return 'Loss'
    elif user_input == 'paper':
        if item == 'rock': return 'Win'
        else: return 'Loss'
    else:
        if item == 'paper': return 'Win'
        else: return 'Loss'

if __name__ == "__main__":
    main()

