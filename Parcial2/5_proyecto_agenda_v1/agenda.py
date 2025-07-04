#Importaciones
import os

#Funciones
def BorrarPantalla():
    os.system("cls")

def EsperarTecla():
    input("\n\t\t\U0001F552 Presiona 'enter' para continuar \U0001F552")

def Menu():
    print("\t\t\U0000260E -\| Sistema de Gestión de Agenda de Contactos |/- \U0000260E")
    op=input("\n\t \U00000031Agregar \n\t \U00000032Mostrar \n\t \U00000033Buscar \n\t \U00000034Eliminar \n\t \U00000035Moificar \n\t \U00000036Salir \n\n \U000027A1 Elige una opción (1-6): ")
    return op

def AgregarContacto(dat):
    BorrarPantalla()
    print("\n\t\t\U0001F4C2 -\|Agregar Contactos|/- \U0001F4C2")
    nom=input(" \U0001F4DD Introduce el nombre del contacto: ").upper().strip()
    if nom not in dat:
        tel=input(" \U0001F4DE Introduce el número telefónico: ").lower().strip()
        mail=input(" \U0001F4E7 Ingrese el correo electrónico: ").lower().strip()
        dat[nom]=[tel,mail]
        print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
    else:
        print("\n\t\t\u26A0 ---Este contacto ya existe--- \u26A0")

def MostrarContacto(dat):
    BorrarPantalla()
    print("\n\t\t\U0001F4DC -\|Lista de contactos|/- \U0001F4DC")
    if not dat:
        print("\n\t\t\u274C ---No hay contactos registrados en la agenda--- \u274C")
    else:
        cont=0
        print(f"{'Nombre':<15} {'Teléfono':<15} {'Correo electrónico':<25} \n{'_'*60}")
        for nom,list in dat.items():
            print(f"{nom:<15} {list[0]:<15} {list[1]:<15}")
            cont+=1
        print(f"{'_'*60} \n\n\t\U0001F4C2 Hay {cont} contactos")
        print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
        
def BuscarContacto(dat):
    BorrarPantalla()
    print("\n\t\t\U0001F50D -\|Buscar contactos|/- \U0001F4C2")
    if not dat:
        print("\n\t\t\u274C ---No hay contactos registrados en la agenda--- \u274C")
    else:
        nom=input("\U0001F50D Ingrese el nombre del contacto a buscar: ").upper().strip()
        noen=True
        for nomb,list in dat.items():
            if nom == nomb:
                print(f"{'Nombre':<15} {'Teléfono':<15} {'Correo electrónico':<25} \n{'_'*60}")
                print(f"{nom:<15} {list[0]:<15} {list[1]:<15} \n{'_'*60}")
                noen=False
        if noen:
            print("\n\t\t\u26A0 ---Este contacto no se encuentra en la lista--- \u26A0")
        else:
            print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")

def BorrarContacto(dat):
    BorrarPantalla()
    print("\n\t\t\U0001F4DB -\|Borrar Contactos|/- \U0001F4DB")
    if not dat:
        print("\n\t\t\u274C ---No hay contactos registrados en la agenda--- \u274C")
    else:
        nom=input("\n \U0001F4DB Ingrese el nombre del contacto a borrar: ").upper().strip()
        for nomb in list(dat):
            if nomb==nom:
                print(f"\n\t\t \U0001F4C2 Datos actuales: \nNombre: {nomb} \nNúmero telefónico: {dat[nomb][1]} \nCorreo electrónico: {dat[nomb][1]}")
                opc=input(f"\u26A0 ¿Desea borrar el contacto {nomb}? (si/no): ").lower().strip()
                if opc=="si":
                    dat.pop(nomb)
                    print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
                else:
                    print("\n\t\t\u2705 ---Acción abortada con éxito--- \u2705")
            else:
                print("\n\t\t\u26A0 ---Este contacto no se encuentra en la lista--- \u26A0")

def ModificarContacto(dat):
    BorrarPantalla()
    print("\n\t\t\U0001F501 -\|Actualizar Contactos|/- \U0001F501")
    if not dat:
        print("\n\t\t\u274C ---No hay contactos registrados en la agenda--- \u274C")
    else:
        nomb=input("\t \U0001F50D Ingrese el nombre del contacto a modificar: ").upper().strip()
        for lis in dat:
            if lis == nomb:
                print(f"\n\t\t \U0001F4C2 Datos actuales: \nNombre: {lis} \nNúmero telefónico: {dat[lis][1]} \nCorreo electrónico: {dat[lis][1]}")
                rep=input(f"\n \u26A0 Desea modificar el contacto {lis}? (si/no): ").lower().strip()
                while rep == "si":
                    print("\t\U0001F501 Ingrese el valor que desea modificar")
                    opc=input("\n\t \U00000031Nombre \n\t \U00000032Teléfono \n\t \U00000033Correo \n\n \U000027A1 Elige una opción (1-3): ")
                    match opc:
                        case "1":
                            nom=input(f"\U0001F501 Ingrese el nuevo nombre del contacto {lis}: ").upper().strip()
                            a=dat.get(lis)
                            dat.pop(lis)
                            dat[nom]=a
                            print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
                        case "2":
                            tel=input(f"\U0001F501 Ingrese el nuevo número del contacto {lis}: ").lower().strip()
                            conta=dat[lis]
                            conta.pop(0)
                            conta.insert(0, tel)
                            print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
                        case "3":
                            mail=input(f"\U0001F501 Ingrese el nuevo correo del contacto {lis}: ").lower().strip()
                            conta=dat[lis]
                            conta.pop(1)
                            conta.insert(1, mail)
                            print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
                        case _:
                            print("\n\t\t\u274C ---Acción no válida--- \u274C")
                    rep=input(f"¿Desea modificar otro dato del contacto {lis}? (si/no): ").lower().strip()
            else:
                print("\n\t\t\u26A0 ---Este contacto no se encuentra en la lista--- \u26A0")