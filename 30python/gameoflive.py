from typing import List
from random import randint as rd
from time import sleep as sp
import os

def PrintGrid(grid:List[List[int]]) -> None:
    print("\033[H", end="")

    for i in grid:
        for j in i:
            print('X', end = ' ') if j > 0 else print(' ', end = ' ')
        print()
    sp(0.2)

def liveCellCount(grid:List[List[int]], x:int, y:int, columns:int, rows:int) -> int:
    temp:List[List[int]] = [[y, x-1],[y, x+1], [y-1, x-1],[y-1,x],[y-1, x+1], [y+1, x-1],[y+1, x],[y+1, x+1]]
    count:int = 0

    for pair in temp:
        if (pair[0] > -1 and pair[0] < rows) and (pair[1] > -1 and pair[1] < columns) and grid[pair[0]][pair[1]] == 1:
            count += 1

    return count

def replaceGrid(grid:List[List[int]], columns:int, rows:int) -> List[List[int]]:
    copyGrid:List[List[int]] = []

    for i in range(rows):
        copyGrid.append([0] * columns)

    for i in range(rows):
        for j in range(columns):
            count:int = liveCellCount(grid, j, i, columns, rows)

            if grid[i][j] == 1:
                if count < 2:
                    copyGrid[i][j] = 0
                elif count == 2 or count == 3:
                    copyGrid[i][j] = 1
                elif count > 3:
                    copyGrid[i][j] = 0
            else:
                if count == 3:
                    copyGrid[i][j] = 1
                else:
                    copyGrid[i][j] = 0

    return copyGrid   

def main() -> None:
    columns: int = 50
    rows:int = 30

    os.system('cls')

    grid:List[List[int]] = []

    for i in range(rows):
        grid.append([0] * columns)
        for j in range(columns):
            grid[i][j] = rd(0,1)

    """grid[rows//2][columns//2-1] = 1
    grid[rows//2][columns//2] = 1
    grid[rows//2][columns//2+1] = 1"""

    """grid[rows // 2][columns//2+1] = 1
    grid[rows // 2+1][columns//2+1] = 1
    grid[rows // 2+1][columns//2] = 1
    grid[rows // 2+1][columns//2-1] = 1
    grid[rows // 2-1][columns//2] = 1"""

    """grid[rows // 2+1][columns//2+1] = 1
    grid[rows // 2+1][columns//2] = 1
    grid[rows // 2-1][columns//2] = 1
    grid[rows//2][columns//2] = 1
    grid[rows//2][columns//2-1] = 1"""


    while True:
        PrintGrid(grid)
        grid = replaceGrid(grid, columns, rows)


main()
    
