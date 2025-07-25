#Importaciones
import os
import mysql.connector

#Entrada a la base de datos
mydb = mysql.connector.connect(
  host="::1",
  user="root",
  password="",
  use_pure=True
)

#Base de datos
def BD():
    mycursor=mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS bd_calificaciones")
    mycursor.execute("USE bd_calificaciones")
    mycursor.execute("SHOW TABLES")
    a=f""
    for x in mycursor:
        a+=f"{x}"
    if "('calificaciones',)" not in a:
        mycursor.execute("CREATE TABLE calificaciones (ID int(25) NOT NULL, Alumnos varchar(100) NOT NULL, Calificacion1 decimal(10,2) NOT NULL, Calificacion2 decimal(10,2) NOT NULL, Calificacion3 decimal(10,2) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
        mycursor.execute("ALTER TABLE calificaciones ADD PRIMARY KEY (ID), ADD KEY id (ID)")
        mycursor.execute("ALTER TABLE calificaciones MODIFY ID int(25) NOT NULL AUTO_INCREMENT;")
        mycursor.execute("COMMIT")

#Funciones
def BorrarPantalla():
    os.system("cls")

def EsperarTecla():
    input("\n\t --- 🕒Pulse enter para continuar🕒 ---")
    BorrarPantalla()

def Menu():
    print("\t\t 📄-\| Sistema de Gestión de Calificaciones |/-📄")
    op=input("\n\t1️⃣ Agregar \n\t2️⃣ Mostrar \n\t3️⃣ Calcular promedios \n\t4️⃣ Buscar \n\t5️⃣ SALIR \n\n👉 Elige una opción (1-5): ")
    return op

def AgregarCalificaciones(dat):
    mycursor=mydb.cursor()
    BorrarPantalla()
    print("\t\t-\|💾 Agregar Calificaciones 💾|/-\n")
    cali=[None]
    nom=input("👤Ingrese el nombre del alumno: ").capitalize().strip()
    cali.append(nom)
    for i in range(1,4):
        ver=True
        while ver:
            try: 
                cal=round(float(input(f"📝Ingrese la calificación número {i}: ")), 2)
                if cal>=0 and cal <=10:
                    cali.append(cal)
                    ver=False
                else:
                    print("---❌ Ingrese un valor comprendido entre el 0 y el 10 ❌---\n")
            except ValueError:
                print("\t---❌ La calificación es un valor numérico ❌---\n") 
    sql=f"INSERT INTO {dat} VALUES(%s, %s, %s, %s, %s)"
    mycursor.execute(sql, cali)
    mydb.commit()
    print("\n\t\t|||✅ La operación se realizó con éxito ✅|||")

def MostrarCalificaciones(dat):
    mycursor=mydb.cursor()
    BorrarPantalla()
    print("\t\t-\|📝 Mostrar las calificaciones 📝|/-\n")
    mycursor.execute(f"SELECT * FROM {dat}")
    myresult = mycursor.fetchall()
    if len(myresult)>0:
        i=len(myresult)
        print(f"{'ID':<5} | {'Nombre':<15} | {'Cal. 1':<10} | {'Cal. 2':<10} | {'Cal. 3':<10}")
        print(f"{'_'*60}")
        for col in myresult:
            print(f"{col[0]:<5}   {col[1]:<15}   {col[2]:<10}   {col[3]:<10}   {col[4]:<10}")
        print(f"{'_'*60}")
        print(f"\nHay un total de {i} alumno(s) registrados\n")
        print("\n\t\t|||✅ La operación se realizó con éxito ✅|||")
    else:
        print("--- ⚠️No hay calificaciones en el sistema⚠️ ---")

def PromediarCalificaciones(dat):
    mycursor=mydb.cursor()
    BorrarPantalla()
    print("\t\t-\|🔄 Promedios 🔄|/-\n")
    mycursor.execute(f"SELECT * FROM {dat}")
    myresult = mycursor.fetchall()
    if len(myresult)>0:
        sum=0
        i=len(myresult)
        print(f"{'Nombre':<15} | {'Promedio':<10}")
        print(f"{'_'*40}")
        for col in myresult:
            nom=col[1]
            prom=(col[2]+col[3]+col[4])/(len(col)-2)
            print(f"{nom:<15} | {prom:<10}")
            sum+=prom
        print(f"{'_'*40}")
        prom_grup=sum/len(myresult)
        print(f"\nHay un total de {i} alumnos registrados y el promedio grupal es de {prom_grup}\n")
        print("\n\t\t|||✅ La operación se realizó con éxito ✅|||")
    else:
        print("--- ⚠️No hay calificaciones en el sistema⚠️ ---")
#Tambien puedes usar prom=sum(col[1:]/len(col)-1)

def BuscarCalificaciones(dat):
    mycursor=mydb.cursor()
    BorrarPantalla()
    print("-\| 🔍Buscar Calificaciones🔍 |/-")
    mycursor.execute(f"SELECT * FROM {dat}")
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        cont=0
        nom=input("Ingrese el nombre del alumno a buscar: ").capitalize().strip()
        var=[nom]
        print(f"{'ID':<5} | {'Nombre':<15} | {'Cal. 1':<10} | {'Cal. 2':<10} | {'Cal. 3':<10}")
        sql = f"SELECT * FROM {dat} WHERE Alumnos = %s"
        mycursor.execute(sql, var)
        myresult = mycursor.fetchall()
        print(f"{'_'*60}")
        for col in myresult:
            if nom==col[1]:
                print(f"{col[0]:<5}   {col[1]:<15}   {col[2]:<10}   {col[3]:<10}   {col[4]:<10}")
                cont+=1
        print(f"{'_'*60}")
        print(f"\n\t\t Son {cont} alumnos con ese nombre")
        print("\n\t\t|||✅ La operación se realizó con éxito ✅|||")
    else:
        print("--- ⚠️No hay calificaciones en el sistema⚠️ ---")
