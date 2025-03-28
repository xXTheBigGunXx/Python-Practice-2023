def function(x):
    all_numbers = [True for _ in range(x+1)]
    y = 2
    while (y*y<=x):
        if all_numbers[y]:      
            for _ in range(y*y, x+1, y):
                all_numbers[_] = False
        y+=1
    for y in range(2, x+1): 
        if all_numbers[y]:
            print(y)
x= 300
function(x)