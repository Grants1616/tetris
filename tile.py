import pygame
import random
from constants import *
import math


class Tile(pygame.sprite.Sprite):
    tile_size = [50, 50]

    shapes = [
        [  # line
            pygame.Rect(-25, -100, 50, 50),
            pygame.Rect(-25, -50, 50, 50),
            pygame.Rect(-25, 0, 50, 50),
            pygame.Rect(-25, 50, 50, 50),
        ],
        [  # T
            pygame.Rect(-75, -50, 50, 50),
            pygame.Rect(-25, -50, 50, 50),
            pygame.Rect(25, -50, 50, 50),
            pygame.Rect(-25, 0, 50, 50),
        ],
        [  # square
            pygame.Rect(-50, -50, 50, 50),
            pygame.Rect(0, -50, 50, 50),
            pygame.Rect(-50, 0, 50, 50),
            pygame.Rect(0, 0, 50, 50),
        ],
        [  # L
            pygame.Rect(-50, -75, 50, 50),
            pygame.Rect(-50, -25, 50, 50),
            pygame.Rect(-50, 25, 50, 50),
            pygame.Rect(0, 25, 50, 50),
        ],
        [  # J
            pygame.Rect(0, -75, 50, 50),
            pygame.Rect(0, -25, 50, 50),
            pygame.Rect(0, 25, 50, 50),
            pygame.Rect(-50, 25, 50, 50),
        ],
        [  # Z
            pygame.Rect(-75, -50, 50, 50),
            pygame.Rect(-25, -50, 50, 50),
            pygame.Rect(-25, 0, 50, 50),
            pygame.Rect(25, 0, 50, 50),
        ],
        [  # S
            pygame.Rect(-25, -50, 50, 50),
            pygame.Rect(25, -50, 50, 50),
            pygame.Rect(-75, 0, 50, 50),
            pygame.Rect(-25, 0, 50, 50),
        ],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(self.shapes)
        self.rotation = 0

    def draw(self, screen):
        for tile in self.type:
            pygame.draw.rect(screen, "white", tile, 2, 2)

    def rotate(self, degree):
        for tile in self.type:
            new_x = (tile.x * math.cos(degree)) - (tile.y * math.sin(degree))
            new_y = (tile.x * math.sin(degree)) + (tile.y * math.cos(degree))
            new_tile = pygame.Rect(new_x, new_y, 50, 50)
            self.type.remove(tile)
            self.type.append(new_tile)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-90)
        if keys[pygame.K_d]:
            self.rotate(90)
