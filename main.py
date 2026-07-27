from typing import Self

import pygame
from constants import *
from tetris_grid import *
from tetromino import *
import numpy as np
import tetromino


def main():
    print("Hello from tetris!")
    print(f"starting tetris with pygame version: {pygame.version.ver}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_matrix = GameGrid()
    game_matrix = game_matrix.create_grid()
    player_piece_exist = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_piece_exist = np.any(game_matrix == 2)
        if player_piece_exist == False:
            piece = Tetrimono()
            piece.get_color()
            piece.get_piece()
            piece.piece_to_matrix()
            piece.matrix_to_screen(game_matrix)
        y = 0
        for row in game_matrix:
            x = 0
            for num in row:
                if num == 5 or num == 6:
                    pygame.draw.rect(
                        screen, "grey", [x, y, NODE_WIDTH, NODE_HEIGHT], 0, 2
                    )
                elif num == 0:
                    pygame.draw.rect(
                        screen, "grey", [x, y, NODE_WIDTH, NODE_HEIGHT], 1, 2
                    )
                elif num == 1 or 2:
                    pygame.draw.rect(
                        screen, piece.color, [x, y, NODE_WIDTH, NODE_HEIGHT], 0, 2
                    )
                x += NODE_WIDTH
            y += NODE_HEIGHT

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
