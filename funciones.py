from clases import *
from cartas import *
from variables import *


def comparar_cartas (carta1:list, carta2:list) -> int:

    #determina quien gano el turno

    if carta1["poder"] > carta2["poder"]:
        return 1
    
    if carta1["poder"] < carta2["poder"]:
        return -1
    
    if carta1["poder"] == carta2["poder"]:
        return 0
    

def puntos_totales (puntos: int, truco:int, jugador1_p: int, jugador2_p: int) -> list:

    #indica como va la tabla

    total = [jugador1_p, jugador2_p]
    

    if puntos > 0:
            total[0] += truco 
        
    elif puntos < 0:
            total[1] += truco

        
    return total


def repartir (mazo:list) -> tuple:
    
    #establece las cartas de cada uno

    #----------jugador----------------
    ima_card1 = (f"cartas/{(mazo[0]["valor"])} de {(mazo[0]["palo"])}.jpg")
    ima_card2 = (f"cartas/{(mazo[1]["valor"])} de {(mazo[1]["palo"])}.jpg")
    ima_card3 = (f"cartas/{(mazo[2]["valor"])} de {(mazo[2]["palo"])}.jpg")



    card1 = jugador ((tamaño_cartas), (400,500), (ima_card1))

    card2 = jugador ((tamaño_cartas), (510,500), (ima_card2))

    card3 = jugador ((tamaño_cartas), (290,500), (ima_card3))

    #-----------------------------

    #---------oponente-----------------

    mano_opo = (mazo[3:6])
    orden_cartas = sorted (mano_opo,key= lambda mano_opo: mano_opo["poder"], reverse = True)
    


    ima_card4 = (f"cartas/{(orden_cartas[0]["valor"])} de {(orden_cartas[0]["palo"])}.jpg")
    ima_card5 = (f"cartas/{(orden_cartas[1]["valor"])} de {(orden_cartas[1]["palo"])}.jpg")
    ima_card6 = (f"cartas/{(orden_cartas[2]["valor"])} de {(orden_cartas[2]["palo"])}.jpg")



    card4 = jugador ((tamaño_cartas), (400,-100), (ima_card4))

    card5 = jugador ((tamaño_cartas), (510,-100), (ima_card5))

    card6 = jugador ((tamaño_cartas), (290,-100), (ima_card6))

    #-----------------------------
    return card1, card2, card3, card4, card5, card6 


def sistemas_puntaje(jugador_1, jugador_2):

    #muestra los puntos en pantalla
     
    puntos_jugador1 = boton ((50,50), (tamaño_puntaje), (azul), (f"jugador 1: {jugador_1}"),(blanco))

    puntos_jugador2 = boton ((700,50), (tamaño_puntaje), (azul), (f"jugador 2: {jugador_2}"),(blanco))

    return puntos_jugador1, puntos_jugador2


def calcular_ganador (jugador_1, jugador_2):
     
     if jugador_1 >= 30:
          resultado = ("GANASTE")
     elif jugador_2 >= 30:
        resultado = ("PERDISTE")
     
     return resultado


    

    

# Función para dibujar texto centrado
def dibujar_texto(texto, fuente, color, superficie, x, y):
    render = fuente.render(texto, True, color)
    rect = render.get_rect(center=(x, y))
    superficie.blit(render, rect)
    return rect 



def valor_envido(carta):
    """Devuelve el valor de envido de una carta."""
    if carta["valor"] in (10, 11, 12):
        return 0
    return carta["valor"]


def calcular_envido(mano):
    """
    Calcula el envido de una mano de 3 cartas.

    """
    mejor = 0
    for i in range(len(mano)):
        for j in range(i + 1, len(mano)):
            if mano[i]["palo"] == mano[j]["palo"]:  # mismo palo
                suma = valor_envido(mano[i]) + valor_envido(mano[j]) + 20
                if suma > mejor:
                    mejor = suma
    if mejor == 0:
        mejor = max(valor_envido(carta) for carta in mano)

    return mejor


def ganador_envido(mano1, mano2):
    """
    Compara dos manos y devuelve:
    - 'Jugador 1' si gana el primero,
    - 'Jugador 2' si gana el segundo,
    - 'Empate' si tienen el mismo puntaje.
    """
    envido1 = calcular_envido(mano1)
    envido2 = calcular_envido(mano2)

    print(f"TANTO Jugador 1: {envido1}")
    print(f"TANTO Jugador 2: {envido2}")

    if envido1 > envido2:
        return "Jugador 1"
    elif envido2 > envido1:
        return "Jugador 2"
    else:
        return "Empate"
