from random import randint

file = open("Desktop/projects/text.txt", "a+")
for x in range(1, 100):
    x = randint(1, 1000)
    file.write(str(x) + " ")
file.close()
file = open("Desktop/python/text.txt", "r")
numbers = file.read().split()
print (numbers)
file.close()

total = 0
for num in numbers:
    total  += int(num)

print (total)
average = total / 100
print (average)

files = "Desktop/projects/text.txt"
file = open(files, "w")
file.write("")
file.close()