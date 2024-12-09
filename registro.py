import csv

FILE_NAME = "personas.csv"

def save_persona(nombre, edad, email):
    if not nombre or not edad.isdigit() or not email:
        print("Datos inválidos")
        return
    
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nombre, edad, email])
    print("Registro guardado:", nombre, edad, email)

def load_persona():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []