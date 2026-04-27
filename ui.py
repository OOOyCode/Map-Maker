import pygame
from support import *
from settings import *

class UI:
    def __init__(self):
        self.display = pygame.display.get_surface()

        self.tile_size = TILE_WIDTH
        self.margin = 5

        self.cols = 10
        self.rows = 10

        self.selected = (0, 0)

        # zone UI
        self.bg = pygame.Rect(
            WIDTH//2 - (self.cols * self.tile_size)//2,
            HEIGHT//3,
            self.cols * self.tile_size,
            self.rows * self.tile_size
        )

    def input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            if self.bg.collidepoint(mx, my):
                x = (mx - self.bg.x) // self.tile_size
                y = (my - self.bg.y) // self.tile_size

                if 0 <= x < self.cols and 0 <= y < self.rows:
                    self.selected = (x, y)

    def draw(self):
        # background UI
        pygame.draw.rect(self.display, "darkgray", self.bg)

        # draw tiles
        for y in range(self.rows):
            for x in range(self.cols):

                tile_img = get_tile(x, y, 16, 16)
                tile_img = pygame.transform.scale(tile_img, (self.tile_size, self.tile_size))

                pos = (
                    self.bg.x + x * self.tile_size,
                    self.bg.y + y * self.tile_size
                )

                self.display.blit(tile_img, pos)

                # border
                rect = pygame.Rect(pos[0], pos[1], self.tile_size, self.tile_size)
                pygame.draw.rect(self.display, "black", rect, 1)

                # highlight selected
                if (x, y) == self.selected:
                    pygame.draw.rect(self.display, "yellow", rect, 3)