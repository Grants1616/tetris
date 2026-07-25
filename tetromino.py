import pygame
import random
import numpy as np


class Tetrimono:
    def __init__(self):
        self.shape_type = ["I", "T", "L", "J", "S", "Z", "O"]
        self.color = ["red", "greeen", "yellow", "blue", "orange"]
        self.matrix = []

    def get_piece(self):
        self.shape_type = random.choice(self.shape_type)

    def get_color(self):
        random.choice(self.color)

    def piece_to_matrix(self):
        if self.shape_type == "I":
            self.matrix = np.array(
                [
                    [0, 0, 0, 0],
                    [2, 2, 2, 2],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                ]
            )
        elif self.shape_type == "J":
            self.matrix = np.array(
                [
                    [2, 0, 0],
                    [2, 2, 2],
                    [0, 0, 0],
                ]
            )
        elif self.shape_type == "L":
            self.matrix = np.array(
                [
                    [0, 0, 2],
                    [2, 2, 2],
                    [0, 0, 0],
                ]
            )
        elif self.shape_type == "O":
            self.matrix = np.array(
                [
                    [2, 2],
                    [2, 2],
                ]
            )
        elif self.shape_type == "Z":
            self.matrix = np.array(
                [
                    [2, 2, 0],
                    [0, 2, 2],
                    [0, 0, 0],
                ]
            )
        elif self.shape_type == "S":
            self.matrix = np.array(
                [
                    [0, 2, 2],
                    [2, 2, 0],
                    [0, 0, 0],
                ]
            )
        elif self.shape_type == "J":
            self.matrix = np.array(
                [
                    [0, 2, 0],
                    [2, 2, 2],
                    [0, 0, 0],
                ]
            )
        return self.matrix

    def matrix_to_screen(self, gameMatrix):
        row_start, col_start = 1, 5
        row_end, col_end = self.matrix.shape
        gameMatrix[row_start : row_start + row_end, col_start : col_start + col_end] = (
            self.matrix
        )
