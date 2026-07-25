import pygame
from constants import *
from main import *
import numpy as np

game_matrix = np.zeros((ROWS, COLUMNS), dtype=int)
for row in game_matrix:
    row[0] = 6
    row[-1] = 6
end_row = [
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
]
game_matrix = np.vstack([game_matrix, end_row])


def drawSquare(screen, x, y, color):
    pygame.draw.rect(screen, color, [x, y, NODE_WIDTH, NODE_HEIGHT], 0, 2)
