"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("cls")

paises=["Mexico","Brasil","Canada","España"]

pais1={
          "nombre":"Mexico",
          "capital":"CDMX",
          "poblacion":12000000,
          "idioma":"español",
          "status":True,
        }

pais2={
          "nombre":"Brasil",
          "capital":"Brasilia",
          "poblacion":14000000,
          "idioma":"portugues",
          "status":True,
        }

pais3={
          "nombre":"Canada",
          "capital":"Ottawa",
          "poblacion":10000000,
          "idioma":["ingles","frances"],
          "status":True,
        }

pais4={
          "nombre":"España",
          "capital":"Madrid",
          "poblacion":11000000,
          "idioma":"español",
          "status":True,
        }

#Imprimir
print("\n\tPais 1:")
for posicion in pais1:
    print(f"{posicion}: {pais1[posicion]}")

#Agregar un atributo a un objeto
pais1["altitud"]=3000
print("\n\tPais 1:")
for posicion in pais1:
    print(f"{posicion}: {pais1[posicion]}")

#Modificar un valor de un item/atributo ya existente
pais1.update({"altitud":2500})
print("\n\tPais 1:")
for posicion in pais1:
    print(f"{posicion}: {pais1[posicion]}")

#Eliminar items
#Manera 1 - Específico
pais1.pop("altitud")
print("\n\tPais 1:")
for posicion in pais1:
    print(f"{posicion}: {pais1[posicion]}")

#Manera 2 - El último elemento
pais1["altitud"]=2500
pais1.popitem()
print("\n\tPais 1:")
for posicion in pais1:
    print(f"{posicion}: {pais1[posicion]}")
