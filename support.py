import pygame
from os.path import *

def get_tile(x, y, tile_size_x, tile_size_y):
    tileset = pygame.image.load(join("assets", "sprites", "world_tileset.png")).convert_alpha()

    rect = pygame.Rect(
        x * tile_size_x,
        y * tile_size_y,
        tile_size_x,
        tile_size_y
    )

    return tileset.subsurface(rect)