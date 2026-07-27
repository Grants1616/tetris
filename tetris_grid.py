import pygame
from constants import *
from main import *
import numpy as np


class GameGrid:
    def __init__(self):
        self.matrix = np.zeros((ROWS, COLUMNS), dtype=int)

    def create_grid(self):
        for row in self.matrix:
            row[0] = 6
            row[-1] = 6
        end_row = [
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
        ]
        self.matrix = np.vstack([self.matrix, end_row])
        return self.matrix

    def shapeFall(self):
        for row in self.matrix[::-1]:
            for num in row:
                if num == 2:
                    x, y = np.where(num)
                    num_below = self.matrix[x + 1][y]
                    if num_below == 0:
                        num_below = 2
                        num = 0
