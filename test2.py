import pygame
import sys
from funciones import *
from imports import *


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
clock = pygame.time.Clock()

#----------Superficies----------------     
cartas = repartir (mazo)

ima_continuar = ("imagenes/flecha.png")

continuar = jugador (tamaño_boton_continuar, (1000,300), ima_continuar)

cantar_truco = boton ((100,500),tamaño_boton_truco, (azul, rojo), ("TRUCO"), (blanco))




#mixer.music.load('imagenes\Truco.ogg')
#mixer.music.set_volume(1)


puntajes = sistemas_puntaje(jugador_1, jugador_2)

#-----------------------------
mano = 1
punto = 0
truco = 1
jugador_1 = 0
jugador_2 = 0

#-----------------


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
        
        clock.tick(fps)

    

    if mano == 0:

          #Muestra como va el marcador
          #reparte las cartas
          #restablece los valores en default

          puntajes = sistemas_puntaje(jugador_1, jugador_2)
          continuar.mover(mano)

          random.shuffle(mazo)
          
          cartas = repartir (mazo)

          punto = 0

          truco = 1

          cantar = False

          mano = 1
         
         
 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

     #pantalla   
    VENTANA.fill(verde_oscuro)
    icono = pygame.image.load("imagenes/tuki.png")
    pygame.display.set_caption("UTN Truco")
    pygame.display.set_icon (icono) 

     #cartas jugador 1
    VENTANA.blit(cartas[0].superficie,cartas[0].rec)

    VENTANA.blit(cartas[1].superficie,cartas[1].rec)

    VENTANA.blit(cartas[2].superficie,cartas[2].rec)

     #cartas jugador 2
    VENTANA.blit(cartas[3].superficie,cartas[3].rec)

    VENTANA.blit(cartas[4].superficie,cartas[4].rec)

    VENTANA.blit(cartas[5].superficie,cartas[5].rec)

     #boton continuar
    VENTANA.blit(continuar.superficie,continuar.rec)

     #boton truco
    VENTANA.blit (cantar_truco.superficie,cantar_truco.rec)

    VENTANA.blit (cantar_truco.texto, (60, 492))

     #puntaje
    VENTANA.blit (puntajes[0].superficie,puntajes[0].rec)

    VENTANA.blit (puntajes[0].texto, (10, 42))

    VENTANA.blit (puntajes[1].superficie,puntajes[1].rec)

    VENTANA.blit (puntajes[1].texto, (660, 42))
   

    if evento.type == pygame.MOUSEMOTION:
         
         #detecta cuando el mouse esta en colicion con el boton truco
         if cantar_truco.rec.collidepoint(evento.pos):
              cantar_truco.superficie.fill(cantar_truco.color_colision)
         else:
              cantar_truco.superficie.fill(cantar_truco.color) 
          


    if evento.type == pygame.MOUSEBUTTONDOWN:
            
               #si jugador preciona el boton truco duplica el puntaje que va a ganar solo una vez por mano
            if cantar_truco.rec.collidepoint(evento.pos) and cantar == False:
                 #audio
                 #mixer.music.play()
                 truco = 2
                 cantar = True

                 
            

           
            if cartas[0].rec.collidepoint(evento.pos):
                 
                 #movimiento carta 1
                 
                 cartas[0].mover(mano)
                 
                 cartas[3].respuesta(mano)

                 turno = comparar_cartas (mazo[0], mazo[3])

                 punto += turno
                 

                 mano +=1

                 
                 
            
            if cartas[1].rec.collidepoint(evento.pos):
                 
                 #movimiento carta 2
                 cartas[1].mover(mano)
                 
                 cartas[4].respuesta(mano)

                 turno = comparar_cartas (mazo[1], mazo[4])

                 punto += turno
                

                 mano +=1

            
            if cartas[2].rec.collidepoint(evento.pos):
                 
                 #movimiento carta 3
                 cartas[2].mover(mano)
                 
                 cartas[5].respuesta(mano)

                 turno = comparar_cartas (mazo[2], mazo[5])

                 punto += turno
                 

                 mano +=1
          
               
            if mano == 4:
                    
                    #finaliza la mano y calcula el puntaje
                    total = puntos_totales (punto, truco, jugador_1, jugador_2)
                    
                    
                    jugador_1 = total[0]
                    jugador_2 = total[1]

                    print ("--------------------------")

                    print (f"player 1: {jugador_1}")
                    print (f"player 2: {jugador_2}")

                    print ("------------------------------")

                    
                    if jugador_1 >= 30 or jugador_2 >= 30:

                         mano = 5    
                    else: 
                         continuar.mover(mano)
                    
                         #permite continuar al jugador a la siguiente mano
                         if continuar.rec.collidepoint(evento.pos):

                      
                              mano = 0
            
          
    if mano == 5:
         
         resultado = calcular_ganador (jugador_1, jugador_2)
         
         if resultado == ("GANASTE"):
               VENTANA.fill(verde)

         elif resultado ==("PERDISTE"):
              VENTANA.fill(rojo)

         print (resultado)



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