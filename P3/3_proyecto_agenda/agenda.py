#Importaciones
import os
import mysql.connector

#Inicio de sesión
mydb = mysql.connector.connect(
  host="::1",
  user="root",
  password="",
  use_pure=True
)

#Base de datos
def BD():
    mycursor=mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS bd_agenda")
    mycursor.execute("USE bd_agenda")
    mycursor.execute("SHOW TABLES")
    a=f""
    for x in mycursor:
        a+=f"{x}"
    if "('agenda',)" not in a:
        mycursor.execute("CREATE TABLE agenda (ID int(25) NOT NULL, Nombre varchar(100) NOT NULL, Telefono varchar(10) NOT NULL, Correo varchar(100) NOT NULL)")
        mycursor.execute("ALTER TABLE agenda ADD PRIMARY KEY (ID), ADD KEY id (ID)")
        mycursor.execute("ALTER TABLE agenda MODIFY ID int(25) NOT NULL AUTO_INCREMENT;")
        mydb.commit()
        
#Uso de la tabla
def TablaApropiada():
    mycursor=mydb.cursor()
    mycursor.execute("SHOW TABLES")
    myresult = mycursor.fetchall()
    myresult = myresult[0][0]
    return myresult

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
    mycursor=mydb.cursor()
    BorrarPantalla()
    print("\n\t\t\U0001F4C2 -\|Agregar Contactos|/- \U0001F4C2")
    nom=input(" \U0001F4DD Introduce el nombre del contacto: ").upper().strip()
    mycursor.execute(f"SELECT Nombre FROM {dat}")
    myresult=mycursor.fetchall()
    a=True
    for x in myresult:
        if nom in x:
            a=False
    if a:
        tel=input(" \U0001F4DE Introduce el número telefónico: ").lower().strip()
        mail=input(" \U0001F4E7 Ingrese el correo electrónico: ").lower().strip()
        sql=f"INSERT INTO agenda VALUES (%s, %s, %s, %s)"
        var=(None, nom, tel, mail)
        mycursor.execute(sql, var)
        mydb.commit()
        print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
        a=False
    else:
        print("\n\t\t\u26A0 ---Este contacto ya existe--- \u26A0")
        a=True

def MostrarContacto(dat):
    mycursor=mydb.cursor()
    BorrarPantalla()
    print("\n\t\t\U0001F4DC -\|Lista de contactos|/- \U0001F4DC")
    mycursor.execute(f"SELECT * FROM {dat}")
    myresult=mycursor.fetchall()
    if not myresult:
        print("\n\t\t\u274C ---No hay contactos registrados en la agenda--- \u274C")
    else:
        cont=0
        print(f"{'Nombre':<15} {'Teléfono':<15} {'Correo electrónico':<25} \n{'_'*60}")
        for contact in myresult:
            print(f"{contact[1]:<15} {contact[2]:<15} {contact[3]:<25}")
            cont+=1
        print(f"{'_'*60} \n\n\t\U0001F4C2 Hay {cont} contactos")
        print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
        
def BuscarContacto(dat):
    mycursor=mydb.cursor()
    BorrarPantalla()
    print("\n\t\t\U0001F50D -\|Buscar contactos|/- \U0001F4C2")
    mycursor.execute(f"SELECT * FROM {dat}")
    myresult=mycursor.fetchall()
    if not myresult:
        print("\n\t\t\u274C ---No hay contactos registrados en la agenda--- \u274C")
    else:
        nom=input("\U0001F50D Ingrese el nombre del contacto a buscar: ").upper().strip()
        mycursor.execute(f"SELECT Nombre FROM {dat}")
        myresult2=mycursor.fetchall()
        a=False
        for x in myresult2:
            if nom in x:
                a=True
        if a:
            print(f"{'Nombre':<15} {'Teléfono':<15} {'Correo electrónico':<25} \n{'_'*60}")
            for nomb in myresult:
                if nom in nomb:
                    print(f"{nomb[1]:<15} {nomb[2]:<15} {nomb[3]:<15}")
            print(f"{'_'*60}\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
        else:
            print("\n\t\t\u26A0 ---Este contacto no se encuentra en la lista, regresando al menú--- \u26A0")


def BorrarContacto(dat):
    mycursor=mydb.cursor()
    BorrarPantalla()
    print("\n\t\t\U0001F4DB -\|Borrar Contactos|/- \U0001F4DB")
    mycursor.execute(f"SELECT * FROM {dat}")
    myresult=mycursor.fetchall()
    if not myresult:
        print("\n\t\t\u274C ---No hay contactos registrados en la agenda--- \u274C")
    else:
        nom=input("\n \U0001F4DB Ingrese el nombre del contacto a borrar: ").upper().strip()
        mycursor.execute(f"SELECT Nombre FROM {dat}")
        myresult2=mycursor.fetchall()
        a=False
        for x in myresult2:
            if nom in x:
                a=True
        if a:
            for nomb in myresult:
                if nom in nomb:
                    print(f"\n\t\t \U0001F4C2 Datos actuales: \nNombre: {nomb[1]} \nNúmero telefónico: {nomb[2]} \nCorreo electrónico: {nomb[3]}")
                    opc=input(f"\u26A0 ¿Desea borrar el contacto {nomb[1]}? (si/no): ").lower().strip()
                    if opc=="si":
                        sql=f"DELETE FROM {dat} WHERE Nombre = %s"
                        var=[nom]
                        mycursor.execute(sql, var)
                        mydb.commit()
                        print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
                    else:
                        print("\n\t\t\u2705 ---Acción abortada con éxito--- \u2705")
        else:
            print("\n\t\t\u26A0 ---Este contacto no se encuentra en la lista--- \u26A0")

def ModificarContacto(dat):
    mycursor=mydb.cursor()
    BorrarPantalla()
    print("\n\t\t\U0001F501 -\|Actualizar Contactos|/- \U0001F501")
    mycursor.execute(f"SELECT * FROM {dat}")
    myresult=mycursor.fetchall()
    if not myresult:
        print("\n\t\t\u274C ---No hay contactos registrados en la agenda--- \u274C")
    else:
        nomb=input("\t \U0001F50D Ingrese el nombre del contacto a modificar: ").upper().strip()
        a=False
        for x in myresult:
            if nomb in x:
                a=True
        nom=nomb
        if a:
            rep="si"
            redun=False
            while rep == "si":
                nomb=nom
                sql=f"SELECT * FROM {dat} WHERE Nombre = %s"
                var=[nomb]
                mycursor.execute(sql, var)
                myresult2=mycursor.fetchall()
                for x in myresult2:
                    print(f"\n\t\t \U0001F4C2 Datos actuales: \nNombre: {x[1]} \nNúmero telefónico: {x[2]} \nCorreo electrónico: {x[3]}")
                    if not redun:
                        rep=input(f"\n \u26A0 Desea modificar el contacto {x[1]}? (si/no): ").lower().strip()
                    if rep=="si":
                        print("\t\U0001F501 Ingrese el valor que desea modificar")
                        opc=input("\n\t \U00000031Nombre \n\t \U00000032Teléfono \n\t \U00000033Correo \n\n \U000027A1 Elige una opción (1-3): ")
                        a=True
                        match opc:
                            case "1":
                                nom=input(f"\U0001F501 Ingrese el nuevo nombre del contacto {x[1]}: ").upper().strip()
                                sql=f"UPDATE {dat} SET Nombre = %s WHERE Nombre = %s"
                                var=[nom, nomb]
                                mycursor.execute(sql, var)
                                mydb.commit()
                                print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
                                a=False
                            case "2":
                                act="Telefono"
                            case "3":
                                act="Correo"
                            case _:
                                print("\n\t\t\u274C ---Acción no válida--- \u274C")
                                a=False
                        if a:
                            new=input(f"\U0001F501 Ingrese el nuevo {act} del contacto {x[1]}: ").lower().strip()
                            sql=f"UPDATE {dat} SET {act} = %s WHERE Nombre = %s"
                            var=[new, nomb]
                            mycursor.execute(sql, var)
                            mydb.commit()
                            print("\n\t\t\u2705 |||Acción realizada con éxito||| \u2705")
                        rep=input(f"¿Desea modificar otro dato del contacto {x[1]}? (si/no): ").lower().strip()
                        if rep=="si":
                            redun=True
        else:
            print("\n\t\t\u26A0 ---Este contacto no se encuentra en la lista--- \u26A0")