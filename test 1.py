new_list = [1,2,3,4]
count_dict = {}

for num in new_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for nums,count in count_dict.items():
    print(count)
