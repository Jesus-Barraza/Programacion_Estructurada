"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("cls")

paises=["Mexico","Brasil","España","Canada","Canada"]
print(paises)
paises=set(paises)
print(paises)

varios={True,"UTD",33,3.14}
print(varios)

#Funciones/operaciones
paises.add("México") #Agrega un elemento al set
print(paises)

paises.pop() #Elimina un elemento al azar del set
print(paises)

paises.add("México")
paises.remove("México") #Elimina un valor en concreto del set
print(paises)

'''Ejemplo: Crear un programa que solicite los email de los alumnos de la UTD, almacenar en una lista
y posteriormente mostrar en pantalla los email sin duplciados'''

#Limpiar lo de la actividad anterior
os.system("cls")

#Creación de valores
emails=[]
r=1

#Introducción de correos
while r!=2:
  print("\n\t\t\033[0m Programa de Emails de la UTD\033[0m")
  emails.append(str(input("\n\nIntroduzca el correo electrónico del alumno: ")).lower())
  r=int(input("\n\t ¿Desea añadir otro correo? \n(1)si \n(2)no \n(1/2): "))

#Impresión
emails=set(emails)
emails=list(emails)
print(emails)
