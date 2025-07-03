'''La lista beta contiene las siguientes funciones:
1.- Nombre comercial
2.- Nombre del compuesto
3.- Caducidad
4.- medida (mililitros o miligramos)
5.- Presentación
6.- Cantidad
7.- Precio al público
8.- Laboratorio'''

#Importaciones
import os
import platform
from datetime import datetime

#Funciones
def BorrarPantalla():
    s = platform.system()
    if s == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def EsperarTecla():
    input("\n\n\t\t \U0001F552 ...Presiona enter para continuar... \U0001F552")

def menu_principal():
    print("\n \U0001F4DD .::Sistema de Gestion de Inventario de Farmacia::. \U0001F4DD \n\t 1.-Agregar \n\t 2.-Borrar \n\t 3.-Mostrar \n\t 4.-Buscar \n\t 5.-Vendido \n\t 6.-Salir")
    opcion = input("Elige una opcion (1-6): ")
    return opcion

def AgregarMedicina(dat):
    BorrarPantalla()
    buff=[]
    print("\n\t\t \U0001F4BE .::Agregar medicina::. \U0001F4BE\n")
    nom=input(" \U0001F4DD Ingresa el nombre comercial de la medicina: ").capitalize().strip()
    buff.append(nom)
    buff.append(input("\n \U0001F4DD Ingresa el nombre del compuesto de la medicina\n(En caso de ser más de uno, separar por un diagonal '/')\n ").capitalize().strip())
    buff.append(input("\n \U0001F4C5 Ingresa la fecha de caducidad de la medicina (mmm/yyyy): ").capitalize().strip())
    print("")
    volver=True
    while volver:
        try:
            med=int(input(" \U0001F4DD Ingrese la medida de la medicina (ml/mg) (solo número): "))
        except ValueError:
            print("\u274C Operación no válida, ingrese solo números \u274C ")
        else:
            buff.append(med)
            volver=False
    buff.append(input("\n \U0001F4DD Ingrese la presentación de la medicina: ").capitalize().strip())
    volver=True
    print("")
    while volver:
        try:
            can=int(input(f" \U0001F4DD Ingrese la cantidad de medicina en {buff[4]} (solo número): "))
        except ValueError:
            print("\u274C Operación no válida, ingrese solo números \u274C ")
        else:
            buff.append(can)
            volver=False
    volver=True
    print("")
    while volver:
        try:
            pre=round(float(input(" \U0001F4DD Ingrese el precio de la medicina ($) (solo número): ")), 2)
        except ValueError:
            print("\u274C Operación no válida, ingrese solo números \u274C ")
        else:
            buff.append(pre)
            volver=False
    buff.append(input("\n \U0001F4DDIngrese el laboratorio donde fue presentado: ").capitalize().strip())
    dat[f"{nom}{med}"]=buff
    print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")

def BorrarMedicina(dat):
    BorrarPantalla()
    print("\n\t\t \U0001F4DB .::Borrar registros del medicamento::. \U0001F4DB")
    nom=input("\n \U0001F50D Ingrese el nombre comercial del medicamento a borrar: ").capitalize().strip()
    med=input("\n \U0001F50D Ingrese el peso o el volúmen de la medicina (ml/mg) (solo números): ").strip()
    sea=nom+med
    if sea not in dat:
        print("\n\t\t \u26A0Este medicamento no se encuentra en la lista\u26A0")
    else:
        cont=0
        for pos in list(dat.keys()):
            if pos==sea:
                print("\n\t \U0001F4C2 Se encontró un medicamento \U0001F50D ")
                opc=input(f"\n¿Desea borrar el registro del medicamento {pos}? (Si/No)").capitalize().strip()
                if opc=="Si":
                    print(f"\n\t \U0001F4DB Se borró el medicamento {pos} \U0001F4DB")
                    del dat[pos]
                    cont+=1
        print(f"\n\t \U0001F4DB Se borraron {cont} registros")  
        print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")

def MostrarMedicina(dat):
    BorrarPantalla()
    print("\n\t\t \U0001F4DC .::Lista de medicamentos registrados::. \U0001F4DC")
    if len(dat) > 0:
        i=len(dat)
        print(f"{"Nombre":<15} | {"Compuesto":<35} | {"Caducidad":<10} | {"Cantidad (mg/ml)":<20} | {"Presentación":<15} | {"Cantidad (presentación)":<25} | {"Precio ($)":<10} | {"Laboratorio":<10}")
        print(f"{"___"*60}")
        for col in dat:
            a=dat.get(col)
            print(f"{a[0]:<15} | {a[1]:<35} | {a[2]:<10} | {a[3]:<20} | {a[4]:<15} | {a[5]:<25} | {a[6]:<10} | {a[7]:<10}")
        print(f"{"___"*60}")
        print(f"\n\t \U0001F50D Hay un total de {i} medicamentos registrados \U0001F50D")
        print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")
    else:
        print("\n\t\t \u274C ...No hay medicina en el sistema... \u274C")

def BuscarMedicina(dat):
    BorrarPantalla()
    print("\n\t\t \U0001F50D .::Buscar Medicamentos::. \U0001F50D ")
    if len(dat) > 0:
        nom=input("\n \U0001F50D Ingrese el nombre comercial del medicamento: ").capitalize().strip()
        med=input("\n \U0001F50D Ingrese el peso o el volúmen de la medicina (ml/mg) (solo números): ").strip()
        sea=nom+med
        if sea not in dat:
            print("\n\t\t \u26A0Este medicamento no se encuentra en la lista\u26A0")
        else:
            cont=0
            print(f"{"Nombre":<15} | {"Compuesto":<35} | {"Caducidad":<10} | {"Cantidad (mg/ml)":<20} | {"Presentación":<15} | {"Cantidad (presentación)":<25} | {"Precio ($)":<10} | {"Laboratorio":<10}")
            print(f"{"___"*60}")
            for pos in dat:
                if pos==sea:
                    a=dat.get(pos)
                    print(f"{a[0]:<15} | {a[1]:<35} | {a[2]:<10} | {a[3]:<20} | {a[4]:<15} | {a[5]:<25} | {a[6]:<10} | {a[7]:<10}")
                    cont+=1
            print(f"{"___"*60}")
            print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")
    else:
        print("\n\t\t \u274C ...No hay medicina en el sistema... \u274C")           

#Funciones que serán trasladadas eventualmente
def AcumulacionVentas(dat):
    BorrarPantalla()
    print("\n\t\t \U00000024 .::Cálculo de acumulación de ventas::. \U00000024")
    if len(dat) > 0:
        total=0
        cont=0
        for i in dat:
            a=dat.get(i)
            corr=True
            while corr:
                try:
                    cant=int(input(f"\n \U0001F4DD Ingrese la cantidad de productos que se vendieron de {i}: "))
                except ValueError:
                    print("\u274C Operación no válida, ingrese solo números \u274C ")
                else:
                    corr=False
            vent=a[6]*cant
            total+=vent
            cont+=cant
        print(f"\n\t \U00000024 Se ha ganado un total de ${total} con la venta de {cont} productos")
        print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")
    else:
        print("\n\t\t \u274C ...No hay medicina en el sistema, por ende, no pudo haber ventas... \u274C")
    
if __name__ == "__main__":
    
    pass

'''Funciones par agregar a futuro'''
#def FechaCaducidad(dat):
#    BorrarPantalla()
#    print("Lista de fecha de medicamentos")
#    if len(dat) > 0:
#        fecha=datetime.now()
#        mes="%B"
#        año="%Y"
#        print(f"Fecha de hoy: {mes}")
#
#def ModificarAtributos(dat):
