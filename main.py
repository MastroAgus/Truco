
from imports import *
from funciones import *
import pygame.mixer as mixer
from archivo import *


pygame.init()
mixer.init()


#----------Superficies----------------
cartas = repartir (mazo)

ima_continuar = ("imagenes/flecha.png")

continuar = jugador (tamaño_boton_continuar, (1000,300), ima_continuar)

cantar_truco = boton ((100,500),tamaño_boton_truco, (azul, rojo), ("TRUCO"), (blanco))

ver_lista_player = boton ((700,500),tamaño_boton_truco, (azul, rojo), ("LISTA"), (blanco))


#mixer.music.load('imagenes\Truco.ogg')
#mixer.music.set_volume(1)


puntajes = sistemas_puntaje(jugador_1, jugador_2)

#for i in range (len(player)):
 #    nom = []
  #   nom[i] = boton ((700,(300+ i*10)),tamaño_boton_truco, (azul), (player[i]), (blanco))


#-----------------------------





pantalla = pygame.display.set_mode ((ancho,alto))



clock = pygame.time.Clock()



mano = 1
punto = 0
truco = 1
jugador_1 = 0
jugador_2 = 0


while run == True:
    clock.tick(fps)

    

    if mano == 0:

          #Muestra como va el marcado
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

     #puntaje
    pantalla.blit (puntajes[0].superficie,puntajes[0].rec)

    pantalla.blit (puntajes[0].texto, (10, 42))

    pantalla.blit (puntajes[1].superficie,puntajes[1].rec)

    pantalla.blit (puntajes[1].texto, (660, 42))

     #lista de jugadores
    pantalla.blit (ver_lista_player.superficie, ver_lista_player.rec)
    pantalla.blit (ver_lista_player.texto, (660, 492))




   

    if evento.type == pygame.MOUSEMOTION:
         
         #detecta cuando el mouse esta en colicion con el boton truco
         if cantar_truco.rec.collidepoint(evento.pos):
              cantar_truco.superficie.fill(cantar_truco.color_colision)
         else:
              cantar_truco.superficie.fill(cantar_truco.color) 
          
         if ver_lista_player.rec.collidepoint(evento.pos):
              ver_lista_player.superficie.fill(ver_lista_player.color_colision)
         else:
              ver_lista_player.superficie.fill(ver_lista_player.color)


    if evento.type == pygame.MOUSEBUTTONDOWN:
            
               #si jugador preciona el boton truco duplica el puntaje que va a ganar solo una vez por mano
            if cantar_truco.rec.collidepoint(evento.pos) and cantar == False:
                 #audio
                 #mixer.music.play()
                 truco = 2
                 cantar = True

            if ver_lista_player.rec.collidepoint(evento.pos):
                 
                 print (player)
               # for i in range (len(player)):
                    #  pantalla.blit (nom[i].superficie, nom[i].rec)
                    # pantalla.blit (nom[i].texto, (660, (292+i*10)))
                 
                 
                 
            

           
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
               pantalla.fill(verde)

         elif resultado ==("PERDISTE"):
              pantalla.fill(rojo)

         print (resultado)


        
          
               
               
         

               
                 
                 






    pygame.display.update()

pygame.quit()