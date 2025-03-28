from random import shuffle as sh
X = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
new_list= []
for num in range(1, 11):
    new_list.append(num)
    sh(new_list)
print(new_list)

def weight(new_list):
    total = 0
    for i in range(len(new_list)):
        total += X[i]*new_list[i]
    return total

print (weight(new_list))
