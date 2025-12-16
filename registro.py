import pygame
import csv
import os
import sys
from funciones import dibujar_texto
from variables import *

ARCHIVO = "personas.csv"

pygame.init()
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Registro de Personas con Puntos")

fuente = pygame.font.SysFont(None, 36)
fuente_lista = pygame.font.SysFont(None, 28)







def leer_puntos():
    """Lee el archivo CSV y devuelve un diccionario {nombre: puntos}."""
    datos = {}
    if not os.path.exists(ARCHIVO):
        return datos
    with open(ARCHIVO, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # salta encabezado
        for row in reader:
            if len(row) >= 2:
                nombre, puntos = row[0], int(row[1])
                datos[nombre] = puntos
    return datos



def guardar_puntos(datos):
    """Guarda el diccionario {nombre: puntos} en el CSV."""
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Puntos"])
        for nombre, puntos in datos.items():
            writer.writerow([nombre, puntos])



def registrar_nombre(nombre):
    """Agrega o actualiza el puntaje de una persona."""
    datos = leer_puntos()
    nombre = nombre.strip().capitalize()
    if nombre in datos:
        datos[nombre] += 1
    else:
        datos[nombre] = 1
    guardar_puntos(datos)



def mostrar_lista():
    """Muestra la lista de personas y sus puntos ordenada por puntaje."""
    datos = leer_puntos()
    datos_ordenados = sorted(datos.items(), key=lambda x: x[1], reverse=True)

    ejecutando = True
    clock = pygame.time.Clock()

    while ejecutando:
        pantalla.fill(blanco)
        titulo = fuente.render("Ranking:", True, negro)
        pantalla.blit(titulo, (20, 20))

        y = 70
        for nombre, puntos in datos_ordenados:
            texto = fuente_lista.render(f"- {nombre}: {puntos} punto{'s' if puntos != 1 else ''}", True, azul)
            pantalla.blit(texto, (40, y))
            y += 30

        salir = fuente_lista.render("(Presiona ESC o cierra la ventana)", True, (80, 80, 80))
        pantalla.blit(salir, (20, ALTO - 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(30)




def registrador ():
    texto = ""


    while True:
            
            
            pantalla.fill(verde)
            WIN = dibujar_texto ("GANASTE", fuente, negro, pantalla, ancho//2, 100 ) 
            titulo = fuente.render("Ingrese tu  nombre:", True, negro)
            pantalla.blit(titulo, (20, 120)) 
            caja = fuente.render(texto, True, azul) 
            pantalla.blit(caja, (40, 150))
 
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and texto.strip() != "":
                            registrar_nombre(texto)
                            mostrar_lista()  
                        elif event.key == pygame.K_BACKSPACE:
                            texto = texto[:-1]
                        elif event.unicode.isprintable():
                            texto += event.unicode

            pygame.display.flip()

 
