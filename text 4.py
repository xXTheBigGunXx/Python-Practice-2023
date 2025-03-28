board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
]

def isValidSudoku(board):

    output = True

    for index in board:
        for number in index:
            if number == ".":
                continue
            if index.count(number) > 1:
                output = False

    rows = [[] for _ in range(9)]

    for index in board:
        list_index = 0
        for number in index:
            rows[list_index].append(number)
            list_index += 1

    for row in rows:
        for numbers in row:
            if numbers == ".":
                continue
            if row.count(numbers) > 1:
                output = False

    three_cobe_list = [[] for _ in range(9)]

    group_size = 3
    result_list = []

    for row in board:
        for i in range(0, len(row), group_size):
            subgroup = row[i:i + group_size]
            result_list.append(subgroup)

    all_groupped = []
    group_index = 0
    for index in board:
        for number in range(1):
            group_result = result_list[group_index] + result_list[group_index + 3] + result_list[group_index + 6]
            all_groupped.append(group_result)
        group_index += 1

    seen = []
    for number_ in all_groupped:
        if number_ != ".":
            continue
        elif number_ in seen:
            output = False
        seen.append(number_)

    return output

print(isValidSudoku(board))
