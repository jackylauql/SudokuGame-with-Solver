[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/jackylauql/SudokuGame-with-Solver)

# SudokuGame-with-Solver

This is a Sudoku game with a solver built with Python using pygame. Run SudokuGame.py to run the application.

# Instructions
For basic information regarding a Sudoku puzzle, please visit https://en.wikipedia.org/wiki/Sudoku

# Pencil Mode
The application supports penciling numbers down on the boxes before confirmation to record and display all possible numbers on the selected box, to toggle pencil mode, click on the Pencil Mode button near the bottom-right corner of the application.

Numbers keyed in with pencil mode toggled will not be checked for conflicts (see below) or win-condition.

# Conflicts
Whenever there is a conflict between confirmed numbers(numbers not keyed with pencil mode untoggled) in the grid, the conflict will be highlighted in red.

# Win-Condition
When all boxes in the grid are filled with confirmed numbers and no conflict exist, a congraluatory message(changes according to time-out) will be printed.

Time freezes when win-condition is fulfilled.

# Time-out
When the time-limit reaches 0, a time-out message will be printed.

# Solve Button
There is a solve button on the bottom right hand corner that allows you to solve the current puzzle using the backtracking algorithm built within the method.
