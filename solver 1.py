import timeit

def solver(original, guess):
    while guess!= original:
        guess +=1
        print (guess)
    return guess
execution_time = timeit.timeit(lambda: solver(9999, 1), number=1)
print(f"Execution time: {execution_time} seconds")