import random

valores = ["1", "2", "3", "4", "5", "6", "7", "10", "11", "12"]
palos = ["Espada", "Basto", "Oro", "Copa"]
truco = {"1": 14, "2": 9, "3": 10, "4": 1, "5": 2, "6": 3, "7": 12,
        "10": 5, "11": 6, "12": 7}

mazo = []
for valor in valores:
    for palo in palos:
        mazo.append({
            "valor": valor,
            "palo": palo,
            "poder": truco[valor]})



random.shuffle(mazo)



 











