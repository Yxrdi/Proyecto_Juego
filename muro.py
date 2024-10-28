import pygame
from configuracion import *


class Muro(pygame.sprite.Sprite):
    def __init__(self, posicion, grupos):
        super().__init__(grupos)
        self.image = pygame.image.load(
            "../graphics/test/rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=posicion)
