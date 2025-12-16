import pygame
import sys
from funciones import *
from variables import *

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menú de Videojuego")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (100, 100, 100)
AZUL = (0, 120, 255)

# Fuente
fuente = pygame.font.SysFont("Arial", 50)



# Funciones del menú
def menu_principal():
    while True:
        VENTANA.fill(GRIS)

        # Dibujar botones
        titulo = dibujar_texto("MENÚ PRINCIPAL", fuente, BLANCO, VENTANA, ANCHO // 2, 100)
        boton_jugar = dibujar_texto("JUGAR", fuente, AZUL, VENTANA, ANCHO // 2, 250)
        boton_opciones = dibujar_texto("OPCIONES", fuente, AZUL, VENTANA, ANCHO // 2, 350)
        boton_salir = dibujar_texto("SALIR", fuente, AZUL, VENTANA, ANCHO // 2, 450)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    jugar()
                if boton_opciones.collidepoint(evento.pos):
                    opciones()
                if boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def jugar():
    corriendo = True
    while corriendo:
        VENTANA.fill(NEGRO)
        dibujar_texto("JUGANDO...", fuente, BLANCO, VENTANA, ANCHO // 2, ALTO // 2)
        dibujar_texto("Presiona ESC para volver", pygame.font.SysFont("Arial", 25), BLANCO, VENTANA, ANCHO // 2, ALTO - 50)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                corriendo = False

        pygame.display.update()

def opciones():
    corriendo = True
    while corriendo:
        VENTANA.fill((30, 30, 30))
        dibujar_texto("OPCIONES", fuente, BLANCO, VENTANA, ANCHO // 2, ALTO // 2 - 100)
        dibujar_texto("Presiona ESC para volver", pygame.font.SysFont("Arial", 25), BLANCO, VENTANA, ANCHO // 2, ALTO - 50)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                corriendo = False

        pygame.display.update()

# Ejecutar el menú
menu_principal()
