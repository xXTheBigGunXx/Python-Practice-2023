def main():
    Matrix = GridCreation()
    game_over = False;
    friend = True;

    while not game_over:
        name = 'Friend' if friend else 'You'
        char = 'X' if friend else 'O'

        print(f"{name} place a {char}:")
        choice = input("X and Y coordination: ")

        choice = choice.split()
        x, y = int(choice[0]), int(choice[1])

        if Valid(Matrix, x, y):
            Matrix[y][x] = char
            printGrid(Matrix)

            friend = False if friend else True
            game_over = Winner(Matrix)
        else:
            print('Invalid coordinates!')
    print("Winner is ")
    print("Friend") if friend else print("You")

def printGrid(grid):
    for row in grid:
        for item in row:
            print(item, end=' ')
        print()

def GridCreation():
    grid = []

    for _ in range(3):
        temp = []
        for _ in range(3):
            temp.append('.')
        grid.append(temp)
    return grid

def Valid(Matrix, X, Y):
    if Matrix[Y][X] == ".":return True
    return False

def Winner(Matrix):
    for i in range(3):
        x = []
        if (Matrix[i][0] == Matrix[i][1] and Matrix[i][1] == Matrix[i][2] and Matrix[i][0] != '.') or (Matrix[0][i] == Matrix[1][i] and Matrix[1][i] == Matrix[2][i] and Matrix[0][i] != '.'):
            return True

    if (Matrix[0][0] == Matrix[1][1] and Matrix[1][1] == Matrix[2][2] and Matrix[0][0] != '.') or (Matrix[0][2] == Matrix[1][1] and Matrix[1][1] == Matrix[2][0] and Matrix[0][2] != '.'):
        return True
    return False
main()