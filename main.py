import pygame
from settings import *
from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.grid = Grid()
        self.start_game = False
        self.generations = 0

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        if self.start_game:
            self.generations += 1
            print(self.generations)
            for row in self.grid.cells:
                for cell in row:
                    self.grid.check_neighbours(cell)

        for row in self.grid.cells:
            for cell in row:
                if cell.alive:
                    cell.dead = False
                else:
                    cell.dead = True

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.grid.draw_grid(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for row in self.grid.cells:
                    for cell in row:
                        if cell.is_clicked(mx, my):
                            cell.alive = not cell.alive

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start_game = not self.start_game
                if event.key == pygame.K_RETURN:
                    self.grid.randomize()


game = Game()
game.run()


