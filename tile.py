import pygame
from os.path import *
from settings import *
from support import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,  posx, posy, *groups):
        super().__init__(*groups)
        
        self.image = get_tile(4, 4, 16, 16)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=(posx, posy))