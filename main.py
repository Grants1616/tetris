import pygame
from constants import *
from tetris_grid import *
from tetromino import *
import numpy as np


def main():
    print("Hello from tetris!")
    print(f"starting tetris with pygame version: {pygame.version.ver}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    piece = Tetrimono()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        y = 0
        for row in game_matrix:
            x = 0
            for item in row:
                if item != 0:
                    drawSquare(screen, x, y, "grey")
                else:
                    drawSquare(screen, x, y, "black")
                x += NODE_WIDTH
            y += NODE_HEIGHT
        piece.get_piece()
        piece.piece_to_matrix()
        piece.matrix_to_screen(game_matrix)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
