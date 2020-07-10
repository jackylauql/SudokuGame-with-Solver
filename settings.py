width = 900
height = 658
white = (255, 255, 255)
black = (33, 33, 33)
lightorange = (255, 152, 48)
lightred = (247, 178, 178)
grey = (190, 190, 190)
lightgrey = (235, 235, 235)
red = (227, 50, 50)
highlightred = (227, 80, 80)
lightblue = (117, 193, 255)
lighterblue = (189, 225, 255)
blue = (56, 151, 245)
highlightblue = (86, 181, 245)

board = [[0 for x in range(9)] for i in range(9)]
board_width = 630
board_height = 630
cell_size = 70
board_position = (14, 14)

board2 = [
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

right_panel_padding = 50
button_width = (width-board_position[0]-board_width) - right_panel_padding
right_panel_starting_pos = [board_position[0]+board_width+(right_panel_padding//2), board_position[1] + 10]
button_positions = (700, 600)