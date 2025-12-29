import pygame
import sys 

pygame.init()
#Screen Consts
WIDTH = 600
HEIGHT = 600

Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Super-Tic-Tac-Toe - Grid")

#Grid settings 
main_grid = 3
sub_grid = 3


#Color consts
BG = (28,28,30)
Grid_color = (200,200,200)
big_line = (220, 220, 220)
small_line = (120,120, 120)
X_color = (235,64,52)
O_color = (52,152,235)

big_line_width = 6
small_line_width = 2
cell_size = WIDTH // main_grid
sub_cell = cell_size // sub_grid


clock = pygame.time.Clock()

#Game State
super_board = [[[[None for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
current_player = "X"
sub_board_winner = [[None for _ in range(3)] for _ in range(3)]
active_board = None
#Draw Function/*
def draw_super_grid():
    Screen.fill(BG)
    #big grid 
    for i in range(1, main_grid):
        pygame.draw.line(Screen, big_line,(i*cell_size,0),(i*cell_size, HEIGHT), big_line_width)
        pygame.draw.line(Screen, big_line, (0, i*cell_size),(WIDTH, i*cell_size), big_line_width)
    
    #small grid
    for br in range(3):
        for bc in range(3):
            sx= bc * cell_size
            sy = br * cell_size
            for i in range(1,3):
                pygame.draw.line(Screen,small_line,(sx + i * sub_cell, sy),(sx + i * sub_cell, sy + cell_size), small_line_width)
                pygame.draw.line(Screen, small_line, (sx, sy + i * sub_cell), (sx + cell_size, sy + i * sub_cell), small_line_width)
 
def draw_x(main_r,main_c,sub_r,sub_c):
    padding = 15
    x_start = main_c * cell_size + sub_c * sub_cell + padding
    y_start = main_r * cell_size + sub_r * sub_cell + padding
    X_end = x_start + sub_cell - 2 * padding
    y_end = y_start + sub_cell - 2 * padding
    pygame.draw.line(Screen, X_color,(x_start, y_start), (X_end, y_end), 4)
    pygame.draw.line(Screen, X_color,(x_start, y_end), (X_end, y_start), 4)

def draw_o(main_r, main_c,sub_r,sub_c):
    cx = main_c * cell_size + sub_c * sub_cell + sub_cell //2
    cy = main_r * cell_size + sub_r * sub_cell + sub_cell //2
    radius = sub_cell //3
    pygame.draw.circle(Screen, O_color, (cx,cy), radius, 4)

def draw_marks():
    for mr in range(3):
        for mc in range(3):
            for sr in range(3):
                for sc in range(3):
                    mark = super_board[mr][mc][sr][sc]
                    if mark == "X":
                        draw_x(mr,mc,sr,sc)
                    elif mark == "O":
                        draw_o(mr,mc,sr,sc)
def check_3x3_win(board):
    #rows
    for r in range(3):
        if board[r][0] and board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]
    
    #columns
    for c in range(3):
        if board[0][c] and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
        
    #Diagonals
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def check_sub_board_win(main_r, main_c):
    if sub_board_winner[main_r][main_c] is not None:
        return 
    winner = check_3x3_win(super_board[main_r][main_c])
    if winner:
        sub_board_winner[main_r][main_c] = winner
        print(f"Sub-board({main_r},{main_c}) won by {winner}")
def draw_big_mark(main_r, main_c, player):
    padding= 30
    start_x = main_c * cell_size + padding
    start_y = main_r * cell_size + padding
    end_x = (main_c + 1)*cell_size - padding
    end_y = (main_r + 1)*cell_size - padding
    if player == "X":
        pygame.draw.line(Screen, X_color, (start_x, start_y), (end_x, end_y), 8)
        pygame.draw.line(Screen, X_color, (start_x, end_y), (end_x, start_y), 8)
    else:
        center = (main_c * cell_size + cell_size // 2, main_r * cell_size + cell_size // 2)
        radius = cell_size //2 - padding
        pygame.draw.circle(Screen,O_color, center, radius, 8)

def highlight_active_board():
    if active_board is None:
        return

    mr, mc = active_board
    rect = pygame.Rect(
        mc * cell_size,
        mr * cell_size,
        cell_size,
        cell_size
    )
    pygame.draw.rect(Screen, (255, 215, 0), rect, 4)
    
def draw_sub_board_winners():
    for r in range(3):
        for c in range(3):
            if sub_board_winner[r][c]:
                draw_big_mark(r,c, sub_board_winner[r][c])

def check_super_board_win():
    return check_3x3_win(sub_board_winner)

    #INPUT 
def get_cell_from_indices(pos):
    x,y = pos
    main_row = y // cell_size
    main_col = x // cell_size

    sub_col =(x%cell_size)// sub_cell
    sub_row = (y%cell_size)//sub_cell
    return main_row, main_col, sub_row, sub_col

#Main loop
game_over = False
super_winner = None
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mr, mc, sr, sc = get_cell_from_indices(event.pos)

    # 🔒 Enforce forced board rule
            if active_board is not None and (mr,mc) != active_board:
                continue

    # 🔒 Prevent playing in won sub-board
            if sub_board_winner[mr][mc] is not None:
                continue

    # 🔒 Prevent overwriting
            if super_board[mr][mc][sr][sc] is not None:
                continue

    #  Place mark
            super_board[mr][mc][sr][sc]=current_player

    # Check sub-board win
            check_sub_board_win(mr, mc)

    # 🔁 Set next forced board
            if sub_board_winner[sr][sc] is None:
                active_board = (sr, sc)
            else:
                active_board = None

    # Check super board win
            winner =check_super_board_win()
            if winner:
                super_winner = winner
                print("kya fayda jeet ke maths 09 marks mile :)")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"             
                                
    draw_super_grid()
    draw_marks()
    draw_sub_board_winners()
    highlight_active_board()
    pygame.display.flip()
pygame.quit()
sys.exit()

        