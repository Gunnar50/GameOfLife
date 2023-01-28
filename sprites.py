import random

import pygame
from settings import *


class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.alive = False
        self.dead = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, WHITE, (self.x, self.y, TILESIZE, TILESIZE))

    def is_clicked(self, mx, my):
        return self.x <= mx < self.x + TILESIZE and self.y <= my < self.y + TILESIZE


class Grid:
    def __init__(self):
        self.cells = []
        self.create_cells()

    def create_cells(self):
        for x in range(0, WIDTH, TILESIZE):
            row = []
            for y in range(0, HEIGHT, TILESIZE):
                row.append(Cell(x, y))
            self.cells.append(row)

    def is_inside(self, x, y):
        return 0 <= x < ROWS and 0 <= y < COLS

    def check_neighbours(self, cell):
        live_neighbours = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                x_neighbour = (cell.x//TILESIZE) + x
                y_neighbour = (cell.y//TILESIZE) + y
                if not (x == 0 and y == 0):
                    if self.is_inside(x_neighbour, y_neighbour) and not self.cells[x_neighbour][y_neighbour].dead:
                        live_neighbours += 1

        # Any live cell with fewer than two live neighbours dies (referred to as underpopulation).
        # Any live cell with more than three live neighbours dies (referred to as overpopulation).
        # Any live cell with two or three live neighbours lives, unchanged, to the next generation.
        # Any dead cell with exactly three live neighbours comes to life.

        if not cell.alive and live_neighbours == 3:
            cell.alive = True
        elif cell.alive and not (2 <= live_neighbours <= 3):
            cell.alive = False

    def draw_grid(self, screen):
        for row in self.cells:
            for cell in row:
                cell.draw(screen)

        for col in range(0, WIDTH, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (col, 0), (col, HEIGHT))

        for row in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (0, row), (WIDTH, row))

    def randomize(self):
        for row in self.cells:
            for cell in row:
                cell.alive = random.choice([0, 1])
