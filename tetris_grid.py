import pygame
from constants import *
from main import *

game_matrix = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
for row in game_matrix:
    row[0] = 6
    row[-1] = 6
game_matrix.append(
    [
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
)


def drawSquare(screen, x, y, color):
    pygame.draw.rect(screen, color, [x, y, NODE_WIDTH, NODE_HEIGHT])


def createGrid(screen):
    y = 0
    for row in game_matrix:
        x = 0
        for item in row:
            if item == 0:
                drawSquare(screen, x, y, "white")
            else:
                drawSquare(screen, x, y, "grey")

            x += NODE_WIDTH
        y += NODE_HEIGHT
