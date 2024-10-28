import pygame
import sys
from configuracion import *
from nivel import Nivel


class Juego:
    def __init__(self):
        pygame.init()   # inicializacion de pygame

        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

        pygame.display.set_caption("Juego")    # titulo de la ventana
        self.reloj = pygame.time.Clock()    # creando del reloj

        self.nivel = Nivel()

    def correr(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.pantalla.fill("black")  # color de fondo de la ventana
            self.nivel.correr()
            pygame.display.update()  # actualizacion de la ventana
            self.reloj.tick(FPS)  # actualizacion del reloj


if __name__ == "__main__":  # determina si el script actual se está ejecutando como programa principa o si se está importando como un módulo en otro script
    juego = Juego()  # instanciación de la clase
    juego.correr()  # se llama el bucle de juego
