import pygame
import random


class Shape(pygame.sprite.Sprite):
    x = 0
    y = 0

    shapes = (
        [(-50, -50), (50, -50), (50, 50), (-50, 50)],  # square
        [(-25, -100), (25, -100), (25, 100), (-25, 100)],  # rectangle
        [(-50, -75), (0, -75), (00, 25), (50, 25), (50, 75), (-50, 75)],  # L-shape
        [
            (-75, -50),
            (75, -50),
            (75, 0),
            (25, 0),
            (25, 50),
            (-25, 50),
            (-25, 0),
            (-50, 0),
        ],  # T-shape
        [
            (-75, -50),
            (25, -50),
            (25, 0),
            (75, 0),
            (75, 50),
            (-25, 50),
            (-25, 0),
            (-75, 0),
        ],  # Z-shape
        [
            (-25, -50),
            (75, -50),
            (75, 0),
            (25, 0),
            (25, 50),
            (-75, 50),
            (-75, 0),
            (-25, 0),
        ],  # S-shape
        [(0, -75), (50, -75), (50, 75), (-50, 75), (-50, 25), (0, 25)],  # J-shape
    )

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.choice(self.shapes)
        self.rotation = 0

    def draw(self, screen: pygame.Surface):
        center_position = []
        for point_x, point_y in self.shape:
            new_x = point_x + 400
            new_y = point_y + 100
            center_position.append((new_x, new_y))
        pygame.draw.polygon(screen, "white", center_position, 3)
