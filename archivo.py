import csv
from clases import *
from variables import *

player = ""

with open ("registro.csv", newline="") as f:

    data = csv.reader(f, delimiter = ",")
    player = list(data)
    

def ver_players(player):
    for i in range (len(player)):
        print (player[i])
        


    