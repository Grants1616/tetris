import pygame
import random
from constants import *


class Tile(pygame.sprite.Sprite):
    shapes = [
        [  # line
            pygame.Rect(0, 0, 50, 50),
            pygame.Rect(0, 50, 50, 50),
            pygame.Rect(0, 100, 50, 50),
            pygame.Rect(0, 150, 50, 50),
        ],
        [  # T
            pygame.Rect(0, 0, 50, 50),
            pygame.Rect(50, 0, 50, 50),
            pygame.Rect(100, 0, 50, 50),
            pygame.Rect(50, 50, 50, 50),
        ],
        [  # square
            pygame.Rect(0, 0, 50, 50),
            pygame.Rect(50, 0, 50, 50),
            pygame.Rect(0, 50, 50, 50),
            pygame.Rect(50, 50, 50, 50),
        ],
        [  # L
            pygame.Rect(0, 0, 50, 50),
            pygame.Rect(0, 50, 50, 50),
            pygame.Rect(0, 100, 50, 50),
            pygame.Rect(50, 100, 50, 50),
        ],
        [  # J
            pygame.Rect(50, 0, 50, 50),
            pygame.Rect(50, 50, 50, 50),
            pygame.Rect(50, 100, 50, 50),
            pygame.Rect(0, 100, 50, 50),
        ],
        [  # Z
            pygame.Rect(0, 0, 50, 50),
            pygame.Rect(50, 0, 50, 50),
            pygame.Rect(50, 50, 50, 50),
            pygame.Rect(100, 50, 50, 50),
        ],
        [
            pygame.Rect(50, 0, 50, 50),
            pygame.Rect(100, 0, 50, 50),
            pygame.Rect(0, 50, 50, 50),
            pygame.Rect(0, 100, 50, 50),
        ],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pick_rand_shape = random.choice(self.shapes)

    def draw(self, screen):
        for tile in self.pick_rand_shape:
            pygame.draw.rect(screen, "white", tile, 2, 2)
