#Importaciones
import funciones
from datetime import datetime
from BD import *

def AgregarMedicina():
    funciones.BorrarPantalla()
    buff=[]
    print("\n\t\t \U0001F4BE .::Agregar medicina::. \U0001F4BE\n")
    buff.append(input("\n \U0001F4DD Ingresa el nombre comercial de la medicina: ").capitalize().strip())
    buff.append(input("\n \U0001F4DD Ingresa el nombre del compuesto de la medicina\n(En caso de ser más de uno, separar por un diagonal '/')\n ").capitalize().strip())
    volver=True
    while volver:
        try:
            year=(int(input("\n \U0001F4C5 Ingresa el año de la fecha de caducidad de la medicina (solo numeros): ")))
            mes=(int(input(" \U0001F4C5 Ingresa el mes de la fecha de caducidad de la medicina (solo numeros): ")))
            dia=(int(input(" \U0001F4C5 Ingresa el dia de la fecha de caducidad de la medicina (solo numeros): ")))
        except ValueError:
            print("\u274C Operación no válida, ingrese solo números \u274C ")
        else:
            fecha=f"{year}"+"-"+f"{mes}"+"-"+f"{dia}"
            fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
            buff.append(fecha)
            volver=False
    volver=True
    while volver:
        try:
            med=int(input("\n \U0001F4DD Ingrese la concentracion de la medicina (ml/mg) (solo número): "))
        except ValueError:
            print("\u274C Operación no válida, ingrese solo números \u274C ")
        else:
            buff.append(med)
            volver=False
    buff.append(input("\n \U0001F4DD Ingrese la presentación de la medicina: ").capitalize().strip())
    volver=True
    while volver:
        try:
            can=int(input(f"\n \U0001F4DD Ingrese la cantidad de {buff[4]} (solo número): "))
        except ValueError:
            print("\u274C Operación no válida, ingrese solo números \u274C ")
        else:
            buff.append(can)
            volver=False
    volver=True
    while volver:
        try:
            pre=round(float(input("\n \U0001F4DD Ingrese el precio de la medicina ($) (solo número): ")), 2)
        except ValueError:
            print("\u274C Operación no válida, ingrese solo números \u274C ")
        else:
            buff.append(pre)
            volver=False
    buff.append(input("\n \U0001F4DDIngrese el laboratorio donde fue presentado: ").capitalize().strip())
    sql="INSERT INTO medicamentos (Nombre_marca, Compuesto_activo, Caducidad, Concentracion, Presentacion, Cantidad, Precio, Laboratorio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, buff)
    conexion.commit()
    print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")

def BorrarMedicina():
    funciones.BorrarPantalla()
    print("\n\t\t \U0001F4DB .::Borrar registros del medicamento::. \U0001F4DB")
    cursor.execute(f"SELECT Nombre_marca FROM medicamentos")
    dat1=cursor.fetchall()
    if len(dat1) <= 0:
        print("\n\t\t \u26A0 ...No hay medicamentos en la lista... \u26A0")
    else:
        dat1.sort()
        print(dat1)
        rep=True
        while rep:
            nom=input("\n \U0001F50D Ingrese el nombre comercial del medicamento a borrar: ").capitalize().strip()
            cursor.execute(f"SELECT * FROM medicamentos WHERE Nombre_marca = '{nom}'")
            dat=cursor.fetchall()
            nomb=(nom, )
            if nomb not in dat:
                print("\n\t\t \u26A0Este medicamento no se encuentra en la lista\u26A0")
                rep=True
            else:
                rep=False
        for pos in dat:
            if nom in pos:
                print("\n\t \U0001F4C2 Se encontró un medicamento \U0001F50D ")
                opc=input(f"\n¿Desea borrar el registro del medicamento {nom} {pos[4]}? (Si/No): ").capitalize().strip()
                if opc=="Si":
                    print(f"\n\t \U0001F4DB Se borró el medicamento {nom} {pos[4]} \U0001F4DB")
                    cursor.execute(f"DELETE FROM medicamentos WHERE ID = '{pos[0]}'")
                    conexion.commit()
        print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")

def MostrarMedicina():
    funciones.BorrarPantalla()
    print("\n\t\t \U0001F4DC .::Lista de medicamentos registrados::. \U0001F4DC")
    cursor.execute(f"SELECT * FROM medicamentos")
    dat=cursor.fetchall()
    if len(dat) > 0:
        i=len(dat)
        print(f"{"ID":<3} | {"Nombre":<40} | {"Compuesto":<55} | {"Caducidad":<10} | {"Cantidad (mg/ml)":<15} | {"Presentación":<11} | {"Cantidad (presentación)":<22} | {"Precio ($)":<10} | {"Laboratorio":<10}")
        print(f"{"___"*60}")
        for col in dat:
            print(f"{col[0]:<3} | {col[1]:<40} | {col[2]:<55} | {str(col[3]):<10} | {col[4]:<15} | {col[5]:<11} | {col[6]:<22} | {col[7]:<10} | {col[8]:<10}")
        print(f"{"___"*60}")
        print(f"\n\t \U0001F50D Hay un total de {i} medicamentos registrados \U0001F50D")
        print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")
    else:
        print("\n\t\t \u274C ...No hay medicina en el sistema... \u274C")

def BuscarMedicina():
    funciones.BorrarPantalla()
    print("\n\t\t \U0001F50D .::Buscar Medicamentos::. \U0001F50D ")
    cursor.execute(f"SELECT Nombre_marca FROM medicamentos")
    dat=cursor.fetchall()
    if len(dat) > 0:
        rep=True
        while rep:
            nom=input("\n \U0001F50D Ingrese el nombre comercial del medicamento: ").capitalize().strip()
            nomb=(nom, )
            if nomb not in dat:
                print("\n\t\t \u26A0Este medicamento no se encuentra en la lista\u26A0")
                rep=True
            else:
                rep=False
        cont=0
        print(f"{"ID":<3} | {"Nombre":<15} | {"Compuesto":<35} | {"Caducidad":<10} | {"Cantidad (mg/ml)":<20} | {"Presentación":<15} | {"Cantidad (presentación)":<25} | {"Precio ($)":<10} | {"Laboratorio":<10}")
        print(f"{"___"*60}")
        for pos in dat:
            if nomb == pos:
                cursor.execute(f"SELECT * FROM medicamentos WHERE Nombre_marca = '{nom}'")
                a=cursor.fetchone()
                print(f"{a[0]:<3} | {a[1]:<15} | {a[2]:<35} | {str(a[3]):<10} | {a[4]:<20} | {a[5]:<15} | {a[6]:<25} | {a[7]:<10} | {a[8]:<10}")
                cont+=1
        print(f"{"___"*60}")
        print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")
    else:
        print("\n\t\t \u274C ...No hay medicina en el sistema... \u274C")
    
def FechaCaducidad():
    funciones.BorrarPantalla()
    print("\n\t\t \U0001F4C5 .::Lista de fecha de medicamentos::. \U0001F4C5")
    cursor.execute(f"SELECT Nombre_marca, Caducidad FROM medicamentos")
    dat=cursor.fetchall()
    if len(dat) > 0:
        fecha=datetime.now().date()
        dat.sort(key = lambda x: x[1])
        cursor.execute(f"SELECT Caducidad FROM medicamentos where Caducidad < '{str(fecha)}'")
        lista1=cursor.fetchall()
        if len(lista1) > 0:
            print("\n\t \u203C :::ESTE MEDICAMENTO ESTÁ CADUCADO::: \u203C")
            for a, e in dat:
                if e < fecha:
                    e=str(e)
                    cursor.execute(f"SELECT Nombre_marca, Caducidad FROM medicamentos where Caducidad = '{e}' AND Nombre_marca = '{a}'")
                    enlista1=cursor.fetchone()
                    print(f"{enlista1[0]:<35} {str(enlista1[1]):<10}")
                else:
                    break
        cursor.execute(f"SELECT Caducidad FROM medicamentos where Caducidad > '{str(fecha)}'")
        lista2=cursor.fetchall()
        if len(lista2) > 0:
            print("\n\t \U0001F4C5 ...Este medicamento está todavía usable...")
            for a, e in dat:
                if e > fecha:
                    e=str(e)
                    cursor.execute(f"SELECT Nombre_marca, Caducidad FROM medicamentos where Caducidad = '{e}' AND Nombre_marca = '{a}'")
                    enlista2=cursor.fetchone()
                    print(f"{enlista2[0]:<35} {str(enlista2[1]):<10}")
        print("\n\t \u2705 :::La operación se ha realizado con éxito::: \u2705")
    else:
        print("\n\t\t \u274C ...No hay medicina en el sistema... \u274C")
        
def ModificarMedicina():
    funciones.BorrarPantalla()
    print("\n\t\t \U0001F4DB .::Modificar registros del medicamento::. \U0001F4DB")
    cursor.execute(f"SELECT Nombre_marca FROM medicamentos")
    dat1=cursor.fetchall()
    if len(dat1) <= 0:
        print("\n\t\t \u26A0 ...No hay medicamentos en la lista... \u26A0")
    else:
        dat1.sort()
        print(dat1)
        rep=True
        while rep:
            nom=input("\n \U0001F50D Ingrese el nombre comercial del medicamento a borrar: ").capitalize().strip()
            cursor.execute(f"SELECT * FROM medicamentos WHERE Nombre_marca = '{nom}'")
            dat=cursor.fetchone()
            if nom not in dat:
                print("\u26A0 Este elemento no se encuentra en la lista \u26A0")
            else:
                rep=False
            print("\n\t \U0001F4C2 Se encontró un medicamento \U0001F50D ")
            print(dat)
            opc=True
            while opc:
                try:
                    opc=int(input(f"\n¿Qué desea modificar  {nom} {dat[4]}?\n 1.- Nombre comercial\n 2.- Nombre del compuesto\n 3.- Caducidad\n 4.- Peso/volumen (ml/mg)\n 5.- Presentación \n 6.- Cantidad\n 7.- Precio ($)\n 8.- Laboratorio\n (1-8): "))
                except ValueError:
                    print("\u274C Operación no válida, ingrese solo números \u274C ")
                    opc=True
                match opc:
                    case 1:
                        valor="Nombre_marca"
                        opc=False
                    case 2:
                        valor="Compuesto_activo"
                        opc=False
                    case 3:
                        valor="Caducidad"
                        opc=False
                    case 4:
                        valor="Concentracion"
                        opc=False
                    case 5:
                        valor="Presentacion"
                        opc=False
                    case 6:
                        valor="Cantidad"
                        opc=False
                    case 7:
                        valor="Precio"
                        opc=False
                    case 8:
                        valor="Laboratorio"
                        opc=False
                    case _:
                        print("\u274C Operación no válida, ingrese solo números \u274C ")
            new=input(f"\n Ingrese el nuevo valor de {valor}: ").capitalize().strip()
            cursor.execute(f"UPDATE medicamentos SET {valor} = '{new}' WHERE ID = '{dat[0]}'")
            conexion.commit()
        print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")

if __name__ == "__main__":
    
    pass
