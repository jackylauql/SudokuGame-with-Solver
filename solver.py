import random

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

'''def print_answer(grid):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print('--------------------')

        for col in range(9):
            if col % 3 == 0:
                print("|", end="")
            if col == 8:
                print(grid[row][col])
            else:
                print(str(grid[row][col]) + " ", end="")'''


def check_empty(grid, emptyCells):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                emptyCells.append([row, col])


def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num and i != col:
            return False
        if grid[i][col] == num and i != row:
            return False

    minigrid_x = row // 3
    minigrid_y = col // 3

    for x in range(minigrid_x * 3, (minigrid_x * 3) + 3):
        for y in range(minigrid_y * 3, (minigrid_y * 3) + 3):
            if grid[x][y] == num and [x, y] != [row, col]:
                return False

    return True


def solve(grid, empty):
    index = 0
    for cell in empty:
        grid[cell[0]][cell[1]] = 0
    while index < len(empty):
        start = grid[empty[index][0]][empty[index][1]] + 1
        while start < 10 and is_valid(grid, empty[index][0], empty[index][1], start) == False:
            start += 1
        if start == 10:
            grid[empty[index][0]][empty[index][1]] = 0
            index -= 1
        else:
            grid[empty[index][0]][empty[index][1]] = start
            index += 1


def randomize_board(visible_cells, empty_cells, locked_cells):
    zero_board = [[0 for x in range(9)] for i in range(9)]
    locked_cells.clear()
    empty_cells.clear()
    while len(locked_cells) < 7:
        row = (random.randint(0, 8))
        col = (random.randint(0, 8))
        num = (random.randint(1, 9))
        while not is_valid(zero_board, row, col, num):
            num += 1
            if num > 9:
                row = (random.randint(0, 8))
                col = (random.randint(0, 8))
                num = (random.randint(1, 9))
        zero_board[row][col] = num
        locked_cells.add((row, col))
    for row in range(9):
        for col in range(9):
            if zero_board[row][col] == 0:
                empty_cells.append([row, col])
    solve(zero_board, empty_cells)
    while len(locked_cells) < visible_cells:
        row = (random.randint(0, 8))
        col = (random.randint(0, 8))
        locked_cells.add((row, col))
    empty_cells.clear()
    for row in range(9):
        for col in range(9):
            if (row, col) not in locked_cells:
                zero_board[row][col] = 0
                empty_cells.append([row, col])
    return zero_board

