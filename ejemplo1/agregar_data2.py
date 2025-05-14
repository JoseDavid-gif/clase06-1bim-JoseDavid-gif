import pandas as pd
from sqlalchemy.orm import sessionmaker

from crear_base import Saludo
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# Saludos individuales
miSaludo = Saludo()
miSaludo.mensaje = "Hola que tal"
miSaludo.tipo = "informal"

miSaludo2 = Saludo()
miSaludo2.mensaje = "Buenas tardes"
miSaludo2.tipo = "formal"

session.add(miSaludo)
session.add(miSaludo2)

# Leer saludos desde el CSV
df = pd.read_csv("saludos_mundo.csv")

for _, row in df.iterrows():
    saludo = Saludo()
    saludo.mensaje = row["saludo"]
    saludo.tipo = row["tipo"]
    session.add(saludo)

# Confirmar todas las transacciones
session.commit()
