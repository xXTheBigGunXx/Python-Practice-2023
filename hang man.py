from random import choice
words_list = open("C:/Users/matas/Desktop/projects/a.txt.txt", "r")
random_word = choice(words_list.read().splitlines())
print("Random word:", random_word)
abc = ['a', 'e', 'i', 'o', 'u', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'y']
list_new = []
list_let = []
guess = 7
while guess > 0:
    if guess == 0:
        print ("You,re dead!")
        break
    letter = input("\nEnter a letter: ").lower()
    if letter in random_word:
        list_new.append(letter)
        new_ss = random_word
        new_s = "".join(char if char in list_new else "_" for char in new_ss)
        print (new_s)
    elif letter in abc:
        list_let.append(letter)
        print ("Wrong letter!")
        guess =guess  - 1
    else:
        print ("Wrong character!")
    print ('Letter not in a word: ' + str(list_let))
    print (str(guess) + " guesses left!")