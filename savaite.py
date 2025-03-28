import random


word_list = ["apple", "banana", "cherry", "dog", "elephant", "flower", "grape", "happiness", "ice cream", "jazz", "kangaroo", "lemon", "mango", 
"noodle", "orange", "penguin", "quilt", "rainbow", "sunshine", "tiger", "umbrella", "violet", "watermelon", "xylophone", "yellow", "zebra"]

def shufller(word_list):
    change_list = []
    for item in word_list:
        item_list = list(item)
        random.shuffle(item_list)
        shuffle = "".join(item_list)
        change_list.append(shuffle)
    return change_list
shufller(word_list)

def guesses(word_list):
    guess_list = []
    for _ in range(len(word_list)//3):
        random_guess = random.choice(word_list)
        if random_guess in guess_list:
            while random_guess in guess_list:
                random_guess = random.choice(word_list)
        guess_list.append(random_guess)
    return guess_list

def checker():
    empty = []

    for word in word_list:
        empty_set = {}
        for letter in word:
            if letter in empty_set:
                empty_set[letter] +=1
            else:
                empty_set[letter] = 1
        empty.append(empty_set)

    for guess in guesses(word_list):
        empty_dict = {}
        for letter in guess:
            if letter in empty_dict:
                empty_dict[letter] +=1
            else:
                empty_dict[letter] = 1

        if empty_dict in empty:
            filtered_word = set(empty_dict.keys())
            filtered_word = "".join(filtered_word)

            index = word_list.index(guess)
            sorted_word = shufller(word_list)
            original_word = "".join(sorted_word[index])
            print(f"Found word is: {original_word}. Answer is: {guess}.")


checker()