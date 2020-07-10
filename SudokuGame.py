import pygame
import tkinter
from settings import *
from buttons import *
from solver import *
import time


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.board = board2
        self.solver_board = board2
        self.selected = None
        self.mouse_pos = None
        self.font = pygame.font.SysFont('cambria', cell_size // 3, bold=True)
        self.pencil_font = pygame.font.SysFont('cambria', cell_size // 3, bold=True)
        self.locked_cells = set()
        self.empty_cells = []
        self.generate_locked_cells()
        self.key = None
        self.list_of_buttons = []
        self.countdown_timer = time.time() + 2
        self.timer_paused = time.time()
        self.game_over = 5
        self.you_won = False
        self.solve_pressed = False
        self.pencil_mode = False
        self.generate_buttons()
        self.medium_board()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Selecting Cell

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks if mouseclick is on the grid to display selection

                selected = self.mouse_on_grid()
                if selected:
                    self.selected = selected
                else:
                    self.selected = None
                    # Checks if buttons are pressed

                    for button in self.list_of_buttons:
                        if button.highlighted:
                            button.function()

            # Keyboard Inputs

            if event.type == pygame.KEYDOWN:
                if self.selected not in self.locked_cells and self.selected:

                    if event.key == pygame.K_1:
                        if self.pencil_mode:
                            if type(self.board[self.selected[0]][self.selected[1]]) == set:
                                if 1 in (self.board[self.selected[0]][self.selected[1]]):
                                    (self.board[self.selected[0]][self.selected[1]]).remove(1)
                                else:
                                    self.board[self.selected[0]][self.selected[1]].add(1)
                            else:
                                self.board[self.selected[0]][self.selected[1]] = set([1])
                        else:
                            self.board[self.selected[0]][self.selected[1]] = 1

                    elif event.key == pygame.K_2:
                        if self.pencil_mode:
                            if type(self.board[self.selected[0]][self.selected[1]]) == set:
                                if 2 in (self.board[self.selected[0]][self.selected[1]]):
                                    (self.board[self.selected[0]][self.selected[1]]).remove(2)
                                else:
                                    self.board[self.selected[0]][self.selected[1]].add(2)
                            else:
                                self.board[self.selected[0]][self.selected[1]] = set([2])
                        else:
                            self.board[self.selected[0]][self.selected[1]] = 2

                    elif event.key == pygame.K_3:
                        if self.pencil_mode:
                            if type(self.board[self.selected[0]][self.selected[1]]) == set:
                                if 3 in (self.board[self.selected[0]][self.selected[1]]):
                                    (self.board[self.selected[0]][self.selected[1]]).remove(3)
                                else:
                                    self.board[self.selected[0]][self.selected[1]].add(3)
                            else:
                                self.board[self.selected[0]][self.selected[1]] = set([3])
                        else:
                            self.board[self.selected[0]][self.selected[1]] = 3

                    elif event.key == pygame.K_4:
                        if self.pencil_mode:
                            if type(self.board[self.selected[0]][self.selected[1]]) == set:
                                if 4 in (self.board[self.selected[0]][self.selected[1]]):
                                    (self.board[self.selected[0]][self.selected[1]]).remove(4)
                                else:
                                    self.board[self.selected[0]][self.selected[1]].add(4)
                            else:
                                self.board[self.selected[0]][self.selected[1]] = set([4])
                        else:
                            self.board[self.selected[0]][self.selected[1]] = 4

                    elif event.key == pygame.K_5:
                        if self.pencil_mode:
                            if type(self.board[self.selected[0]][self.selected[1]]) == set:
                                if 5 in (self.board[self.selected[0]][self.selected[1]]):
                                    (self.board[self.selected[0]][self.selected[1]]).remove(5)
                                else:
                                    self.board[self.selected[0]][self.selected[1]].add(5)
                            else:
                                self.board[self.selected[0]][self.selected[1]] = set([5])
                        else:
                            self.board[self.selected[0]][self.selected[1]] = 5

                    elif event.key == pygame.K_6:
                        if self.pencil_mode:
                            if type(self.board[self.selected[0]][self.selected[1]]) == set:
                                if 6 in (self.board[self.selected[0]][self.selected[1]]):
                                    (self.board[self.selected[0]][self.selected[1]]).remove(6)
                                else:
                                    self.board[self.selected[0]][self.selected[1]].add(6)
                            else:
                                self.board[self.selected[0]][self.selected[1]] = set([6])
                        else:
                            self.board[self.selected[0]][self.selected[1]] = 6

                    elif event.key == pygame.K_7:
                        if self.pencil_mode:
                            if type(self.board[self.selected[0]][self.selected[1]]) == set:
                                if 7 in (self.board[self.selected[0]][self.selected[1]]):
                                    (self.board[self.selected[0]][self.selected[1]]).remove(7)
                                else:
                                    self.board[self.selected[0]][self.selected[1]].add(7)
                            else:
                                self.board[self.selected[0]][self.selected[1]] = set([7])
                        else:
                            self.board[self.selected[0]][self.selected[1]] = 7

                    elif event.key == pygame.K_8:
                        if self.pencil_mode:
                            if type(self.board[self.selected[0]][self.selected[1]]) == set:
                                if 8 in (self.board[self.selected[0]][self.selected[1]]):
                                    (self.board[self.selected[0]][self.selected[1]]).remove(8)
                                else:
                                    self.board[self.selected[0]][self.selected[1]].add(8)
                            else:
                                self.board[self.selected[0]][self.selected[1]] = set([8])
                        else:
                            self.board[self.selected[0]][self.selected[1]] = 8

                    elif event.key == pygame.K_9:
                        if self.pencil_mode:
                            if type(self.board[self.selected[0]][self.selected[1]]) == set:
                                if 9 in (self.board[self.selected[0]][self.selected[1]]):
                                    (self.board[self.selected[0]][self.selected[1]]).remove(9)
                                else:
                                    self.board[self.selected[0]][self.selected[1]].add(9)
                            else:
                                self.board[self.selected[0]][self.selected[1]] = set([9])
                        else:
                            self.board[self.selected[0]][self.selected[1]] = 9

                    elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        self.board[self.selected[0]][self.selected[1]] = 0

                if self.is_empty():
                    if self.check_win():
                        self.you_won = True

    # Updates mouse position

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        for button in self.list_of_buttons:
            button.update(self.mouse_pos)
            if button.highlighted:
                button.color = button.highlight_color
            else:
                button.color = button.default_color

    # Checks if mouse is on grid

    def mouse_on_grid(self):
        if self.mouse_pos[0] < board_position[0] or self.mouse_pos[1] < board_position[1]:
            return False
        if self.mouse_pos[0] > (board_position[0] + board_width) or self.mouse_pos[1] > (
                board_position[1] + board_height):
            return False
        else:
            return (self.mouse_pos[1] - board_position[0]) // cell_size, (
                    self.mouse_pos[0] - board_position[1]) // cell_size

    # Checks if board is filled up

    def is_empty(self):
        for cell in self.empty_cells:
            if self.board[cell[0]][cell[1]] == 0 or type(self.board[cell[0]][cell[1]]) != int:
                return False
        return True

    # Checks win-condition

    def check_win(self):
        for row in range(9):
            for col in range(9):
                num = self.board[row][col]
                for index in range(9):
                    # Check conflict in same row
                    if self.board[row][index] == num and index != col:
                        return False
                    # Check conflict in same column
                    if self.board[index][col] == num and index != row:
                        return False

                minigrid_row = row // 3
                minigrid_col = col // 3
                # Check conflict in same minigrid-----------------------------something wrong here
                for r in range(minigrid_row * 3, minigrid_row * 3 + 3):
                    for c in range(minigrid_col * 3, minigrid_col * 3 + 3):
                        if self.board[r][c] == num and [r, c] != [row, col]:
                            return False
        return True

    # Drawing Section

    def draw(self):
        self.screen.fill(white)
        if self.selected:
            self.highlight_selected()
            self.check_conflict(self.board)
            self.draw_grid(self.screen)
            self.highlight_input()
        else:
            self.check_conflict(self.board)
            self.draw_grid(self.screen)
        for button in self.list_of_buttons:
            button.draw()
        self.draw_time(self.countdown_timer)
        self.generate_board(self.screen)
        if self.you_won:
            self.draw_win()

        pygame.display.update()

    def draw_win(self):
        message = 'You solved it in time!'
        if self.game_over < 5:
            message = 'You solved it!'
        text = self.font.render('Congratulations!', 1, (0, 255, 0))
        text2 = self.font.render(message, 1, (0, 255, 0))
        text_width = text.get_width()
        text2_width = text2.get_width()
        x_position = (button_width - text_width) // 2 + right_panel_starting_pos[0]
        x_position2 = (button_width - text2_width) // 2 + right_panel_starting_pos[0]
        self.screen.blit(text, (x_position, height - board_position[1] - 350))
        self.screen.blit(text2, (x_position2, height - board_position[1] - 330))

    # Highlights selected cell with an orange border

    def highlight_input(self):
        if (self.selected[0], self.selected[1]) not in self.locked_cells:
            pygame.draw.rect(self.screen, lightorange, (self.selected[1] * cell_size + board_position[0],
                                                        self.selected[0] * cell_size + board_position[1], cell_size,
                                                        cell_size), 3)

    # Highlights row, col and minigrid of selected cell with lightgrey

    def highlight_selected(self):
        row = self.selected[0]
        col = self.selected[1]

        if (self.selected[0], self.selected[1]) not in self.locked_cells:
            pygame.draw.rect(self.screen, lightgrey,
                             (board_position[0] + col * cell_size, board_position[1], cell_size, cell_size * 9))
            pygame.draw.rect(self.screen, lightgrey,
                             (board_position[0], board_position[1] + row * cell_size, cell_size * 9, cell_size))

            minigrid_row = row // 3
            minigrid_col = col // 3

            for r in range(minigrid_row * 3, minigrid_row * 3 + 3):
                for c in range(minigrid_col * 3, minigrid_col * 3 + 3):
                    pygame.draw.rect(self.screen, lightgrey, ((minigrid_col * 3 * cell_size) + board_position[0],
                                                              (minigrid_row * 3 * cell_size) + board_position[1],
                                                              cell_size * 3, cell_size * 3))

    # Time-limit

    def format_time(self, timer):
        minutes = int(round(timer // 60, 0))
        seconds = timer % 60
        return 'Time: ' + str(minutes) + ':' + str(int(round(seconds, 0)))

    def draw_time(self, seconds):
        if not self.solve_pressed and not self.you_won:
            self.timer_paused = time.time()
        self.game_over = seconds - self.timer_paused
        if self.game_over < 0.5:
            self.game_over = 0.5
            timeout = self.font.render('Time is up!', 1, (255, 0, 0))
            timeout_width = timeout.get_width()
            timeout_x_position = (button_width - timeout_width) // 2 + right_panel_starting_pos[0]
            self.screen.blit(timeout, (timeout_x_position, height - board_position[1] - 250))
        countdown = self.format_time(self.game_over)
        timer = self.font.render(countdown, 1, (0, 0, 0))
        timer_width = timer.get_width()
        x_position = (button_width - timer_width) // 2 + right_panel_starting_pos[0]
        self.screen.blit(timer, (x_position, height - board_position[1] - 290))

    # Draws grid-lines

    def draw_grid(self, screen):
        pygame.draw.rect(screen, black, (board_position[0], board_position[1], board_width, board_height), 2)
        for col in range(9):
            if col % 3 == 0:
                pygame.draw.line(screen, black, ((col * cell_size) + board_position[0], board_position[1]),
                                 ((col * cell_size) + board_position[0], board_position[1] + board_height), 3)
            else:
                pygame.draw.line(screen, black, ((col * cell_size) + board_position[0], board_position[1]),
                                 ((col * cell_size) + board_position[0], board_position[1] + board_height), 1)

        for row in range(9):
            if row % 3 == 0:
                pygame.draw.line(screen, black, (board_position[0], ((row * cell_size) + board_position[1])),
                                 (board_position[0] + board_width, (row * cell_size) + board_position[1]), 3)
            else:
                pygame.draw.line(screen, black, (board_position[0], ((row * cell_size) + board_position[1])),
                                 (board_position[0] + board_width, (row * cell_size) + board_position[1]), 1)

    # Function to draw number

    def input_number(self, screen, text, pos, color):
        num = self.font.render(text, False, color)
        num_width = num.get_width()
        num_height = num.get_height()
        pos[0] += (cell_size - num_width) // 2
        pos[1] += (cell_size - num_height) // 2
        screen.blit(num, pos)

    def pencil_number(self, screen, text, pos, color):
        num = self.pencil_font.render(str(text), False, color)
        mini_cell_size = cell_size // 3
        position = 5 + pos[0] + ((text - 1) % 3)*mini_cell_size, pos[1] + ((text - 1) // 3)*mini_cell_size
        screen.blit(num, position)

    # Function to check board and put numbers on screen

    def generate_board(self, screen):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    position = [col * cell_size + board_position[0], row * cell_size + board_position[1]]
                    if (row, col) in self.locked_cells:
                        self.input_number(screen, str(self.board[row][col]), position, black)
                    else:
                        if type(self.board[row][col]) == int:
                            self.input_number(screen, str(self.board[row][col]), position, red)
                        else:
                            for num in self.board[row][col]:
                                self.pencil_number(screen, num, position, blue)

    # Add locked cells

    def generate_locked_cells(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    self.locked_cells.add((row, col))
                elif self.board[row][col] == 0:
                    self.empty_cells.append([row, col])

    # Buttons Section

    def generate_buttons(self):
        easy_button = Buttons(right_panel_starting_pos[0], right_panel_starting_pos[1], button_width, 40, 'Easy', self.easy_board,
                              lightblue, lighterblue, self.screen)
        self.list_of_buttons.append(easy_button)

        medium_button = Buttons(right_panel_starting_pos[0], right_panel_starting_pos[1] + 60, button_width, 40,
                                'Medium', self.medium_board, lightblue, lighterblue, self.screen)
        self.list_of_buttons.append(medium_button)

        hard_button = Buttons(right_panel_starting_pos[0], right_panel_starting_pos[1] + 120, button_width, 40, 'Hard',
                              self.hard_board, lightblue, lighterblue, self.screen)
        self.list_of_buttons.append(hard_button)

        impossible_button = Buttons(right_panel_starting_pos[0], right_panel_starting_pos[1] + 180, button_width, 40,
                                    'Impossible', self.impossible_board, lightblue, lighterblue, self.screen)
        self.list_of_buttons.append(impossible_button)

        pencil_button = Buttons(right_panel_starting_pos[0], height - board_position[1] - 150, button_width, 60,
                                'Pencil Mode: Off',
                                self.toggle_pencil_mode, blue, highlightblue, self.screen)
        self.list_of_buttons.append(pencil_button)

        solve_button = Buttons(right_panel_starting_pos[0], height - board_position[1] - 70, button_width, 60, 'Solve',
                               self.solve_sudoku, red, highlightred, self.screen)
        self.list_of_buttons.append(solve_button)

    def toggle_pencil_mode(self):
        if self.pencil_mode:
            self.pencil_mode = False
            self.list_of_buttons[4].text = 'Pencil Mode: Off'
        else:
            self.pencil_mode = True
            self.list_of_buttons[4].text = 'Pencil Mode: On'

    def solve_sudoku(self):
        solve(self.board, self.empty_cells)
        self.solve_pressed = True

    def easy_board(self):
        new_board = randomize_board(80, self.empty_cells, self.locked_cells)
        self.board = new_board
        self.countdown_timer = time.time() + 599
        self.solve_pressed = False
        self.you_won = False

    def medium_board(self):
        new_board = randomize_board(38, self.empty_cells, self.locked_cells)
        self.board = new_board
        self.countdown_timer = time.time() + 899
        self.solve_pressed = False
        self.you_won = False

    def hard_board(self):
        new_board = randomize_board(35, self.empty_cells, self.locked_cells)
        self.board = new_board
        self.countdown_timer = time.time() + 1199
        self.solve_pressed = False
        self.you_won = False

    def impossible_board(self):
        new_board = randomize_board(28, self.empty_cells, self.locked_cells)
        self.board = new_board
        self.countdown_timer = time.time() + 1199
        self.solve_pressed = False
        self.you_won = False

    # Function to highlight light-red

    def highlight_conflict(self, position, width, height):
        pygame.draw.rect(self.screen, lightred, (position[1], position[0], width, height))

    # Checks for conflict and calls function to highlight them

    def check_conflict(self, board):
        for row in range(9):
            for col in range(9):
                if (row, col) not in self.locked_cells and board[row][col] != 0 and type(board[row][col]) == int :
                    num = board[row][col]
                    for index in range(9):
                        # Check conflict in same row
                        if board[row][index] == num and col != index:
                            self.highlight_conflict(
                                [board_position[0] + row * cell_size, board_position[1] + index * cell_size], cell_size,
                                cell_size)
                        # Check conflict in same column
                        if board[index][col] == num and row != index:
                            self.highlight_conflict(
                                [board_position[0] + index * cell_size, board_position[1] + col * cell_size], cell_size,
                                cell_size)

                    minigrid_row = row // 3
                    minigrid_col = col // 3
                    # Check conflict in same minigrid
                    for r in range(minigrid_row * 3, minigrid_row * 3 + 3):
                        for c in range(minigrid_col * 3, minigrid_col * 3 + 3):
                            if board[r][c] == num and [r, c] != [row, col]:
                                self.highlight_conflict(
                                    [board_position[0] + r * cell_size, board_position[1] + c * cell_size], cell_size,
                                    cell_size)


app = App()
app.run()