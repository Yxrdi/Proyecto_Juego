import pygame
pygame.init()
fuente = pygame.font.Font(None, 30)


def debug(informacion, y=10, x=10):
    mostrar_superficie = pygame.display.get_surface()
    depurar_superficie = fuente.render(str(informacion), True, "White")
    depurar_rectangulo = depurar_superficie.get_rect(arriba_izquierda=(x, y))
    pygame.draw.rect(mostrar_superficie, "Black", depurar_rectangulo)
    mostrar_superficie.blit(depurar_superficie, depurar_rectangulo)
