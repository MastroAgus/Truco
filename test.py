import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ["Espada", "Basto", "Oro", "Copa"]
truco = {1: 14, 2: 9, 3: 10, 4: 1, 5: 2, 6: 3, 7: 12,
        10: 5, 11: 6, 12: 7}

mazo = []
for valor in valores:
    for palo in palos:
        mazo.append({
            "valor": valor,
            "palo": palo,
            "poder": truco[valor]})



random.shuffle(mazo)


mano_player1 = [mazo[0],mazo[1],mazo[2]]

mano_player2 = [mazo[3],mazo[4],mazo[5]]


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


 
"""
print (mano_player1)
print (mano_player2)

print("Ganador del envido:", ganador_envido(mano_player1, mano_player2))

"""