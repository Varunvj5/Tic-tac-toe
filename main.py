import pygame
import sys
import numpy as np

from pygame import draw, init

pygame.init()

# Creating A Gameplay Window

WIDTH = 600
HEIGHT = 600

# ==========
# Constants
# ==========

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_ROWS
CIRCLE_RAD = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (239, 231, 200)
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE//4
CROSS_COLOR = (66, 66, 66)

# Creating TIC TAC TOE Board

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE', 'Centre')
screen.fill(BG_COLOR)


def draw_lines():
    # 1st Horizontal Line
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE),
                     (WIDTH, SQUARE_SIZE), width=10)
    # 2nd Horizontal Line
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE),
                     (WIDTH, 2 * SQUARE_SIZE), width=10)
    # 1st Vertical Line
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0),
                     (SQUARE_SIZE, HEIGHT), width=10)
    # 2nd Vertical Line
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0),
                     (2 * SQUARE_SIZE, HEIGHT), width=10)


board = np.zeros((BOARD_ROWS, BOARD_COLS))

draw_lines()


def mark_sq(row, col, player):
    board[row][col] = player


def available_sq(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

# Code for Circle and Cross Figures


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(
                    col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RAD, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(
                    screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)


def check_winner(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_vertical_winning_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

# Declaring Functions of Strikethorugh Lines


def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(BG_COLOR)
    draw.lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_ROWS):
            board[row][col] = 0


player = 1
game_over = False

# Writing Mainloop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_sq(clicked_row, clicked_col):
                if player == 1:
                    mark_sq(clicked_row, clicked_col, 1)
                    if check_winner(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_sq(clicked_row, clicked_col, 2)
                    if check_winner(player):
                        game_over = True
                    player = 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()
