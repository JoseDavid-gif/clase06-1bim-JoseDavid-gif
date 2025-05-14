from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo


import csv

# Abrir el archivo CSV
with open("data/saludos_mundo.csv", newline='', encoding='utf-8') as csvfile:
    lector = csv.reader(csvfile, delimiter='|')  
    encabezado = next(lector)  
    for fila in lector:
        saludo = fila[0]
        tipo = fila[1]
        origen = fila[2]
        session.add(Saludo2(mensaje =fila[0], tipo =fila[1], origen= fila[2]))



# se confirma las transacciones
session.commit()

