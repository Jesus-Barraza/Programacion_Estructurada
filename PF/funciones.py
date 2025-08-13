#Importaciones
import os
import platform


#Funciones
def BorrarPantalla():
    s = platform.system()
    if s == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def EsperarTecla():
    input("\n\n\t\t \U0001F552 ...Presiona enter para continuar... \U0001F552")

def menu_inventario():
    print("\n \U0001F4DD .::Sistema de Gestion de Inventario de Farmacia::. \U0001F4DD \n\t 1.-Agregar medicamentos \n\t 2.-Borrar medicamentos \n\t 3.-Mostrar medicamentos \n\t 4.-Buscar medicamentos \n\t 5.-Lista de fechas de caducidad \n\t 6.-Modificar la lista de medicamentos \n\t 7.- Regresar al menú principal")
    opcion = input("Elige una opcion (1-6): ")
    return opcion

def menu_usuarios():
   print("\n \t.:: Inicio de sesion ::.. \n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir ")
   opcion=input("\t\t Elige una opción: ").upper().strip() 
   return opcion


   