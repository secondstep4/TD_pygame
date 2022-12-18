import pygame
from settings import *

class Zone(pygame.sprite.Sprite):
    def __init__(self, pos, surface : pygame.Surface, color = (0,0,0),  *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.image = surface
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)