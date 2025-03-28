x = "X"
y = "X"
list_to_do = ["Clean the house: ", x, "Read book: ", y]

input_clean = input("Have you clean the house? ").lower()
input_read = input("Have you read the book? ").lower()

if input_clean == "yes":
    x = "✓"
    list_to_do[1] = x
if input_read == "yes":
    y = "✓"
    list_to_do[3] = y

print(list_to_do[0], list_to_do[1])
print(list_to_do[2], list_to_do[3])

