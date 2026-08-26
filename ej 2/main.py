import pygame
import sys
import os

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escenario con fondo")

directorio_actual = os.path.dirname(__file__)
ruta_imagen = os.path.join(directorio_actual, "cancha de telmo.png")

try:
    fondo_original = pygame.image.load(ruta_imagen).convert()
    fondo = pygame.transform.scale(fondo_original, (ANCHO, ALTO))
except pygame.error as e:
    print(f"No se pudo cargar la imagen: {e}")
    pygame.quit()
    sys.exit()

COLOR_PLATAFORMA = (100, 50, 0)
COLOR_PUERTA = (150, 75, 0)
COLOR_PERSONAJE = (50, 150, 255)

ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.blit(fondo, (0, 0))

    pygame.draw.rect(pantalla, COLOR_PLATAFORMA, (100, 450, 600, 40))
    pygame.draw.rect(pantalla, COLOR_PUERTA, (620, 330, 60, 120))
    pygame.draw.rect(pantalla, COLOR_PERSONAJE, (150, 390, 40, 60))

    pygame.display.flip()
    reloj.tick(1)

pygame.quit()
sys.exit()