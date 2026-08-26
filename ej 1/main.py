import pygame
pygame.init()
ANCHO = 800
ALTO = 500
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menú clickeable")
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    opc_1 = pygame.draw.rect()
    opc_2 = pygame.draw.rect()
    opc_3 = pygame.draw.rect()

