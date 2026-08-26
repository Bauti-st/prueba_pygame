import pygame
import sys
import os

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escena de fútbol")

directorio_actual = os.path.dirname(__file__)

ruta_fondo = os.path.join(directorio_actual, "cancha de telmo.png")
try:
    fondo_original = pygame.image.load(ruta_fondo).convert()
    fondo = pygame.transform.scale(fondo_original, (ANCHO, ALTO))
except pygame.error as e:
    print(f"Error al cargar la imagen de fondo: {e}")
    pygame.quit()
    sys.exit()

ruta_personaje = os.path.join(directorio_actual, "personaje.png")
try:
    personaje_original = pygame.image.load(ruta_personaje).convert_alpha()
    personaje = pygame.transform.scale(personaje_original, (120, 160))
except pygame.error as e:
    print(f"Error al cargar la imagen del personaje: {e}")
    pygame.quit()
    sys.exit()

ruta_arco = os.path.join(directorio_actual, "arco de futbol.png")
try:
    arco_original = pygame.image.load(ruta_arco).convert_alpha()
    arco = pygame.transform.scale(arco_original, (200, 150))
except pygame.error as e:
    print(f"Error al cargar la imagen del arco: {e}")
    pygame.quit()
    sys.exit()

COLOR_PLATAFORMA = (0, 255, 0)

ALTO_PERSONAJE = 160
Y_PISO = 450 - ALTO_PERSONAJE

pos_x = 50
pos_y = Y_PISO
velocidad_x = 5

vel_y = 0
gravedad = 0.8
fuerza_salto = -15
en_suelo = True

ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        pos_x -= velocidad_x
    if teclas[pygame.K_d]:
        pos_x += velocidad_x

    if teclas[pygame.K_SPACE] and en_suelo:
        vel_y = fuerza_salto
        en_suelo = False

    vel_y += gravedad
    pos_y += vel_y

    if pos_y >= Y_PISO:
        pos_y = Y_PISO
        vel_y = 0
        en_suelo = True

    pantalla.blit(fondo, (0, 0))

    pygame.draw.rect(pantalla, COLOR_PLATAFORMA, (0, 450, ANCHO, 150))

    pantalla.blit(arco, (ANCHO - 200, 325))
    pantalla.blit(personaje, (pos_x, pos_y))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()