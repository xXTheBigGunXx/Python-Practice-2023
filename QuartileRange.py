from forpro import median, split_list, new
new_list = [3, 6, 4, 8, 5, 9, 7]
frq = [2, 2, 2, 2, 3, 1, 1]
new_list_2 = []
new_list_3 = []
new_list_4 = []

total =  (new(new_list, frq, new_list_2))
total.sort()
print(total)

middle = median(total)
print ("Mediana",middle)

lenght = len(total)
if lenght % 2 != 0:
    lenght = int(lenght / 2)
    total.remove(lenght - 1)

print (split_list(total, new_list_3, new_list_4))
first = median(new_list_3)
third = median(new_list_4)
con = float(third - first)
print (con)
