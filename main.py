import pygame
import random
import time
import math
from color import *

WIDTH = HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flood-It')
pygame.font.init()

def flood_fill(board, i, j, prev_color, new_color):
    if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] != new_color and board[i][j] == prev_color:
        board[i][j] = new_color
        flood_fill(board, i - 1, j, prev_color, new_color)
        flood_fill(board, i + 1, j, prev_color, new_color)
        flood_fill(board, i, j - 1, prev_color, new_color)
        flood_fill(board, i, j + 1, prev_color, new_color)
    pass

def flooded(board):
    for i in range(len(board) - 1):
        if board[i] != board[i+1]:
            return False
    return True

def gen_board():
    board = row = []
    color = [RED, CYAN, GREEN, PURPLE, PINK, YELLOW]
    for i in range(10):
        row = [color[random.randint(0, 5)] for _ in range(10)]
        board.append(row)
    return board

def draw_board(board):
    for i in range(10):
        for j in range(10):
            cell = pygame.Rect(j*50, i*50, 50, 50)
            pygame.draw.rect(screen, board[i][j], cell)
    
    pygame.display.update()
    pass

def main():
    board = gen_board()
    run = True

    while run:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()  
            color_selected = board[math.floor(mouse_y/50)][math.floor(mouse_x/50)]
            if (board[0][0] == color_selected):
                continue
            flood_fill(board, 0, 0, board[0][0], color_selected)
        
        draw_board(board)
        if flooded(board):
            replay_button = pygame.Rect(WIDTH/2 - 250/2, HEIGHT/2 - 100/2, 250, 100)
            pygame.draw.rect(screen, (255, 255, 255), replay_button)
            font = pygame.font.SysFont('arial', 70)
            replay_text = font.render('REPLAY', True, (0, 0, 0))
            size = pygame.font.Font.size(font, 'REPLAY')
            screen.blit(replay_text, (WIDTH/2 - size[0]/2, HEIGHT/2 - size[1]/2))
            pygame.display.update()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            event = pygame.event.wait()
            if (event.type == pygame.MOUSEBUTTONDOWN and
                replay_button.collidepoint(mouse_x, mouse_y)):
                board = gen_board()
            if (event.type == pygame.MOUSEBUTTONDOWN and
                not replay_button.collidepoint(mouse_x, mouse_y)):
                run = False

main()