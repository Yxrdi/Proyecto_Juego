import pygame
from configuracion import *
from muro import Muro
from jugador import Jugador


class Nivel:
    def __init__(self):
        # visualización de la superficie
        self.mostrar_superficie = pygame.display.get_surface()
        # configuración del grupo de sprites
        self.mostrar_sprites = pygame.sprite.Group()
        self.obstaculos_sprites = pygame.sprite.Group()

        # configuración de sprites
        self.crear_mapa()

    def crear_mapa(self):
        for indice_fila, fila in enumerate(MAPA):
            for índice_columna, columna in enumerate(fila):
                x = índice_columna * TILESIZE
                y = indice_fila * TILESIZE
                if columna == "x":
                    Muro((x, y), [self.mostrar_sprites])

                if columna == "p":
                    Jugador((x, y), [self.mostrar_sprites])

    def correr(self):
        # actualizar y dibujar el juego
        self.mostrar_sprites.draw(self.mostrar_superficie)
