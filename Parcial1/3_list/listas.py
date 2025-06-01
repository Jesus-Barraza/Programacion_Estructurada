import os
os.system("cls")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros=[1,2,3,4,5,6,7,8,9]
print(numeros)

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

palabras=["tabla","momento","ayuda"]
for i in palabras:
    if i=="momento":
        o=True
if o:
    print(f"Se halló la palabra {i}")
else:
    print("No se encontró la palabra")

#Ejemplo 3 Añadir elementos a la lista

e="relleno"
tabla=[]
while e!="n":
    tabla.append(input("Inserta una palabra para añadirla a la lista: "))
    e=input("¿Desea añadir otra palabra? (s/n): ").lower()
print(tabla)

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda= [
    ["Joaquín", 6186489234],
    ["Alejandro", 6183649503],
    ["Pepe", 6189043578]
]

for a in agenda:
    print(str(a))