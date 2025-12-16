
from imports import *
from funciones import *
import pygame.mixer as mixer
import sys
from registro import *
from test import *

pygame.init()
mixer.init()


#----------Superficies----------------     
cartas = repartir (mazo)

ima_continuar = ("imagenes/flecha.png")

continuar = jugador (tamaño_boton_continuar, (1000,300), ima_continuar)

cantar_truco = boton ((100,500),tamaño_boton_truco, (azul, rojo), ("TRUCO"), (blanco))

cantar_envido = boton ((650,500),tamaño_boton_truco, (azul, rojo), ("ENVIDO"), (blanco))

#teet
xd = ""
test = boton((ancho//2,alto//2),tamaño_boton_continuar, (azul, rojo), (xd), (blanco))

#teeet


fuente = pygame.font.SysFont("Arial", 50)

#mixer.music.load('imagenes\Truco.ogg')
#mixer.music.set_volume(1)


puntajes = sistemas_puntaje(jugador_1, jugador_2)



#-----------------------------





pantalla = pygame.display.set_mode ((ancho,alto))



clock = pygame.time.Clock()



mano = 1
punto = 0
truco = 1
jugador_1 = 30
jugador_2 = 29

#contador_mensaje = 0
#mostrar_mensaje = False




while run == True:
    clock.tick(fps)

    mano_player1 = [mazo[0],mazo[1],mazo[2]]

    mano_player2 = [mazo[3],mazo[4],mazo[5]]

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

          mano_player1 = [mazo[0],mazo[1],mazo[2]]

          mano_player2 = [mazo[3],mazo[4],mazo[5]]

          envido = 2 

          tanto = False
         
         
 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

     #pantalla   
    pantalla.fill(verde_oscuro)
    icono = pygame.image.load("imagenes/tuki.png")
    pygame.display.set_caption("UTN Truco")
    pygame.display.set_icon (icono) 

     #cartas jugador 1
    pantalla.blit(cartas[0].superficie,cartas[0].rec)

    pantalla.blit(cartas[1].superficie,cartas[1].rec)

    pantalla.blit(cartas[2].superficie,cartas[2].rec)

     #cartas jugador 2
    pantalla.blit(cartas[3].superficie,cartas[3].rec)

    pantalla.blit(cartas[4].superficie,cartas[4].rec)

    pantalla.blit(cartas[5].superficie,cartas[5].rec)

     #boton continuar
    pantalla.blit(continuar.superficie,continuar.rec)

     #boton truco
    pantalla.blit (cantar_truco.superficie,cantar_truco.rec)

    pantalla.blit (cantar_truco.texto, (60, 492))

#add
    pantalla.blit (cantar_envido.superficie,cantar_envido.rec)

    pantalla.blit (cantar_envido.texto, (610, 492))

    pantalla.blit (test.superficie,test.rec)
    pantalla.blit (test.texto, (ancho//2-40,alto//2 +8 ))

#dda
     #puntaje
    pantalla.blit (puntajes[0].superficie,puntajes[0].rec)

    pantalla.blit (puntajes[0].texto, (10, 42))

    pantalla.blit (puntajes[1].superficie,puntajes[1].rec)

    pantalla.blit (puntajes[1].texto, (660, 42))
   

    if evento.type == pygame.MOUSEMOTION:
         
         #detecta cuando el mouse esta en colicion con el boton truco
         if cantar_truco.rec.collidepoint(evento.pos):
              cantar_truco.superficie.fill(cantar_truco.color_colision)
         else:
              cantar_truco.superficie.fill(cantar_truco.color)
#add
         if cantar_envido.rec.collidepoint(evento.pos):
              cantar_envido.superficie.fill(cantar_envido.color_colision)
         else:
              cantar_envido.superficie.fill(cantar_envido.color)
#dda

    if evento.type == pygame.MOUSEBUTTONDOWN:
            
               #si jugador preciona el boton truco duplica el puntaje que va a ganar solo una vez por mano
            if cantar_truco.rec.collidepoint(evento.pos) and cantar == False:
                 #audio
                 #mixer.music.play()
                 truco = 2
                 cantar = True

#add
            if cantar_envido.rec.collidepoint(evento.pos) and tanto == False:
               
               print (mano_player1)
               print (mano_player2)

              
               
             

               gano_envido = ganador_envido(mano_player1, mano_player2)    
               #print("Ganador del envido:", ganador_envido(mano_player1, mano_player2))

               if gano_envido == ("Jugador 1"):
                    jugador_1 += envido
                    print ((jugador_1))

                    
                    resultado_tanto = dibujar_texto ("GANASTE ENVIDO", fuente, negro, pantalla, ancho//2, 100 )

                    
                    
               
               elif gano_envido == ("Jugador 2"):
                    jugador_2 += envido
                    print ((jugador_2))

                    resultado_tanto = dibujar_texto ("PERDISTE ENVIDO", fuente, negro, pantalla, ancho//2, 100 )
               
               elif gano_envido == ("Empate"):
                    print ("empate")

                    resultado_tanto = dibujar_texto ("EMPATASTE ENVIDO", fuente, negro, pantalla, ancho//2, 100 )


               tanto = True     

#dda
           
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
                         texto = ""   
                    else: 
                         continuar.mover(mano)
                    
                         #permite continuar al jugador a la siguiente mano
                         if continuar.rec.collidepoint(evento.pos):

                      
                              mano = 0
            
              
    while mano == 5:
         
               resultado = calcular_ganador (jugador_1, jugador_2)
               
               if resultado == ("GANASTE"):
                    

              
               #--------------------------------
               
               
                registrador ()

                     
            

               #¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿

               if resultado ==("PERDISTE"):
                    pantalla.fill(rojo)

                    LOSE = dibujar_texto ("PERDISTE", fuente, blanco, pantalla, ancho//2, 100 ) 


               print (resultado) 


        
          
               

    pygame.display.flip()
