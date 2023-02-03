import pygame
import random
import math
from color import *
import argparse

parser = argparse.ArgumentParser(
    description = 'Flood It game written in Python')
parser.add_argument('--size', '-s',
                    type=int, default=500,
                    help='Change board size')
parser.add_argument('--cell', '-c',
                    type=int, default=10,
                    help='Change number of cells of each row/column')
args = parser.parse_args()

WIDTH = HEIGHT = args.size # must <= 780
number_of_cells = args.cell
cell_length = WIDTH / number_of_cells

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flood-It')
pygame.font.init()

def flood_fill(board, i, j, prev_color, new_color):
    if (i >= 0 and i < len(board) and 
        j >= 0 and j < len(board[0]) and 
        board[i][j] != new_color and board[i][j] == prev_color):
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

def gen_board(number_of_cells):
    board = row = []
    color = DRACULA
    for i in range(number_of_cells):
        row = [color[random.randint(0, 5)] 
               for _ in range(number_of_cells)]
        board.append(row)
    return board

def draw_board(board):
    for i in range(number_of_cells):
        for j in range(number_of_cells):
            cell = pygame.Rect(j*cell_length, i*cell_length, 
                               cell_length, cell_length)
            pygame.draw.rect(screen, board[i][j], cell)
    
    pygame.display.update()
    pass

def main():
    board = gen_board(number_of_cells)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            color_selected = board[
                math.floor(mouse_y/cell_length)][
                math.floor(mouse_x/cell_length)]
            flood_fill(board, 0, 0, board[0][0], color_selected)
        
        draw_board(board)
        if flooded(board):
            button_width, button_height = 250, 100
            replay_button = pygame.Rect(WIDTH/2 - button_width/2, 
                                        HEIGHT/2 - button_height/2, 
                                        button_width, button_height)
            pygame.draw.rect(screen, (255, 255, 255), replay_button)
            font = pygame.font.SysFont('arial', 70)
            replay_text = font.render('REPLAY', True, (0, 0, 0))
            text_width, text_height = pygame.font.Font.size(font, 'REPLAY')
            screen.blit(replay_text, (WIDTH/2 - text_width/2, 
                                      HEIGHT/2 - text_height/2))
            pygame.display.update()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            event = pygame.event.wait()
            if (event.type == pygame.MOUSEBUTTONDOWN and
                replay_button.collidepoint(mouse_x, mouse_y)):
                board = gen_board(number_of_cells)
            if (event.type == pygame.MOUSEBUTTONDOWN and
                not replay_button.collidepoint(mouse_x, mouse_y)):
                run = False

main()