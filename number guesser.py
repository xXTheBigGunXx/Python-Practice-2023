input = int(input("What is the number? "))
guess = 1
while True:
    if input == guess:
        break
    elif input != guess:
        guess = guess + 1
print (guess)
