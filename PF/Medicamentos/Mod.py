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
            dia=(int(input(" \U0001F4C5 Ingresa el mes de la fecha de caducidad de la medicina (solo numeros): ")))
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
            med=int(input("\n \U0001F4DD Ingrese la medida de la medicina (ml/mg) (solo número): "))
        except ValueError:
            print("\u274C Operación no válida, ingrese solo números \u274C ")
        else:
            buff.append(med)
            volver=False
    buff.append(input("\n \U0001F4DD Ingrese la presentación de la medicina: ").capitalize().strip())
    volver=True
    while volver:
        try:
            can=int(input(f"\n \U0001F4DD Ingrese la cantidad de medicina en {buff[4]} (solo número): "))
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
    sql="INSERT INTO medicamentos (`nombre de la marca`, `nombre del compuesto activo`, caducidad, `ml/mg`, presentacion, cantidad, `precio al publico`, laboratorio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, buff)
    conexion.commit()
    print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")

def BorrarMedicina():
    funciones.BorrarPantalla()
    print("\n\t\t \U0001F4DB .::Borrar registros del medicamento::. \U0001F4DB")
    cursor.execute(f"SELECT `nombre de la marca` FROM medicamentos")
    dat1=cursor.fetchall()
    if len(dat1) <= 0:
        print("\n\t\t \u26A0Este medicamento no se encuentra en la lista\u26A0")
    else:
        a=[]
        for i in dat1:
            a+=i
        a.sort()
        print(a)
        nom=input("\n \U0001F50D Ingrese el nombre comercial del medicamento a borrar: ").capitalize().strip()
        cursor.execute(f"SELECT * FROM medicamentos WHERE `nombre de la marca` = '{nom}'")
        dat=cursor.fetchall()
        cont=0
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
        print(f"{"ID":<3} | {"Nombre":<25} | {"Compuesto":<60} | {"Caducidad":<10} | {"Cantidad (mg/ml)":<20} | {"Presentación":<15} | {"Cantidad (presentación)":<25} | {"Precio ($)":<10} | {"Laboratorio":<10}")
        print(f"{"___"*60}")
        for col in dat:
            print(f"{col[0]:<3} | {col[1]:<25} | {col[2]:<60} | {str(col[3]):<10} | {col[4]:<20} | {col[5]:<15} | {col[6]:<25} | {col[7]:<10} | {col[8]:<10}")
        print(f"{"___"*60}")
        print(f"\n\t \U0001F50D Hay un total de {i} medicamentos registrados \U0001F50D")
        print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")
    else:
        print("\n\t\t \u274C ...No hay medicina en el sistema... \u274C")

def BuscarMedicina():
    funciones.BorrarPantalla()
    print("\n\t\t \U0001F50D .::Buscar Medicamentos::. \U0001F50D ")
    cursor.execute(f"SELECT `nombre de la marca` FROM medicamentos")
    dat=cursor.fetchall()
    if len(dat) > 0:
        nom=input("\n \U0001F50D Ingrese el nombre comercial del medicamento: ").capitalize().strip()
        nomb=(nom, )
        if nomb not in dat:
            print("\n\t\t \u26A0Este medicamento no se encuentra en la lista\u26A0")
        else:
            cont=0
            print(f"{"ID":<3} | {"Nombre":<15} | {"Compuesto":<35} | {"Caducidad":<10} | {"Cantidad (mg/ml)":<20} | {"Presentación":<15} | {"Cantidad (presentación)":<25} | {"Precio ($)":<10} | {"Laboratorio":<10}")
            print(f"{"___"*60}")
            for pos in dat:
                if nomb == pos:
                    cursor.execute(f"SELECT * FROM medicamentos WHERE `nombre de la marca` = '{nom}'")
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
    cursor.execute(f"SELECT `nombre de la marca`, caducidad FROM medicamentos")
    dat=cursor.fetchall()
    if len(dat) > 0:
        fecha=datetime.now().date()
        dat.sort(key = lambda x: x[1])
        cursor.execute(f"SELECT caducidad FROM medicamentos where caducidad < '{str(fecha)}'")
        lista1=cursor.fetchall()
        if len(lista1) > 0:
            print("\n\t \u203C :::ESTE MEDICAMENTO ESTÁ CADUCADO::: \u203C")
            for a, e in dat:
                if e < fecha:
                    e=str(e)
                    cursor.execute(f"SELECT `nombre de la marca`, caducidad FROM medicamentos where caducidad = '{e}' AND `nombre de la marca` = '{a}'")
                    enlista1=cursor.fetchone()
                    print(f"{enlista1[0]:<35} {str(enlista1[1]):<10}")
                else:
                    break
        cursor.execute(f"SELECT caducidad FROM medicamentos where caducidad > '{str(fecha)}'")
        lista2=cursor.fetchall()
        if len(lista2) > 0:
            print("\n\t \U0001F4C5 ...Este medicamento está todavía usable...")
            for a, e in dat:
                if e > fecha:
                    e=str(e)
                    cursor.execute(f"SELECT `nombre de la marca`, caducidad FROM medicamentos where caducidad = '{e}' AND `nombre de la marca` = '{a}'")
                    enlista2=cursor.fetchone()
                    print(f"{enlista2[0]:<35} {str(enlista2[1]):<10}")
        print("\n\t \u2705 :::La operación se ha realizado con éxito::: \u2705")
    else:
        print("\n\t\t \u274C ...No hay medicina en el sistema... \u274C")

if __name__ == "__main__":
    
    pass

#Funciones que serán trasladadas eventualmente
#def AcumulacionVentas(dat):
#    funciones.BorrarPantalla()
#    print("\n\t\t \U00000024 .::Cálculo de acumulación de ventas::. \U00000024")
#    if len(dat) > 0:
#        total=0
#        cont=0
#        for i in dat:
#            a=dat.get(i)
#            corr=True
#            while corr:
#                try:
#                    cant=int(input(f"\n \U0001F4DD Ingrese la cantidad de productos que se vendieron de {i}: "))
#                except ValueError:
#                    print("\u274C Operación no válida, ingrese solo números \u274C ")
#                else:
#                    corr=False
#            vent=a[6]*cant
#            total+=vent
#            cont+=cant
#        print(f"\n\t \U00000024 Se ha ganado un total de ${total} con la venta de {cont} productos")
#        print("\n\n\t\t \u2705 :::La operación se ha realizado con éxito::: \u2705")
#    else:
#        print("\n\t\t \u274C ...No hay medicina en el sistema, por ende, no pudo haber ventas... \u274C")