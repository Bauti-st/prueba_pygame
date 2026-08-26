import pygame
pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi juego")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 180, 0)
AZUL = (0, 100, 200)
ROJO = (200, 0, 0)

fuente = pygame.font.Font(None, 50)

MENU = 0
JUEGO = 1
INSTRUCCIONES = 2

estado = MENU
jugando = True

boton_jugar = pygame.Rect(245, 200, 320, 70)
boton_instrucciones = pygame.Rect(245, 300, 320, 70)
boton_salir = pygame.Rect(245, 400, 320, 70)

while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            if estado == MENU:
                if boton_jugar.collidepoint(mouse):
                    estado = JUEGO
                if boton_instrucciones.collidepoint(mouse):
                    estado = INSTRUCCIONES
                if boton_salir.collidepoint(mouse):
                    jugando = False
            elif estado == JUEGO:
                estado = MENU
            elif estado == INSTRUCCIONES:
                estado = MENU
            if estado == MENU:
                pantalla.fill(NEGRO)

                pygame.draw.rect(pantalla, VERDE, boton_jugar)
                pygame.draw.rect(pantalla, AZUL, boton_instrucciones)
                pygame.draw.rect(pantalla, ROJO, boton_salir)

                texto = fuente.render("JUGAR", True, BLANCO)
                pantalla.blit(texto, (350, 220))

                texto = fuente.render("INSTRUCCIONES", True, BLANCO)
                pantalla.blit(texto, (258, 320))

                texto = fuente.render("SALIR", True, BLANCO)
                pantalla.blit(texto, (350, 420))
        elif estado == JUEGO:
            pantalla.fill(VERDE)

            texto = fuente.render("¡ESTAS JUGANDO!", True, BLANCO)
            pantalla.blit(texto, (245, 250))

            texto = fuente.render("Click para volver", True, BLANCO)
            pantalla.blit(texto, (260, 350))

        elif estado == INSTRUCCIONES:
            pantalla.fill(AZUL)

            texto = fuente.render("INSTRUCCIONES", True, BLANCO)
            pantalla.blit(texto, (270, 150))

            texto = fuente.render("Presiona JUGAR para iniciar el juego", True, BLANCO)
            pantalla.blit(texto, (100, 250))

            texto = fuente.render("Click para volver al menu", True, BLANCO)
            pantalla.blit(texto, (200, 350))
    pygame.display.flip()

pygame.quit()