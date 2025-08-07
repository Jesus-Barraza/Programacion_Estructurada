import mysql.connector
import csv
ruta="F:/Archivo/Proyecto_Final/tabla_medicamentos.csv"

try:
    conexion=mysql.connector.connect(
        host="::1",
        user="root",
        password="",
        database="farmacia",
        use_pure=True
    )
    confirm=True
    print("Conexión exitosa")
    cursor=conexion.cursor(buffered=True)
except mysql.connector.errors.ProgrammingError:
    try:
        conexion=mysql.connector.connect(
            host="::1",
            user="root",
            password="",
            use_pure=True
        )
        cursor=conexion.cursor(buffered=True)
    except:
        print(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ...") 
        confirm=False
    else:
        cursor.execute("CREATE DATABASE farmacia")
        cursor.execute("USE farmacia")
        print("Se creó la base de datos")
        confirm=True
except:
    print(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ...") 
    confirm=False

def tabla_med_upd():
    try:
        a=True
        while a:
            try:
                cursor.execute("SELECT * FROM medicamentos")
                x=cursor.fetchall()
            except mysql.connector.errors.InterfaceError:
                a=True
            else:
                a=False
        if len(x) <= 0 or x == None:
            with open(ruta, mode='r', encoding='utf-8') as archivo:
                lector_csv = csv.reader(archivo)
                fila1=next(lector_csv)
                for fila in lector_csv:
                    sql = f"INSERT INTO medicamentos (`{fila1[0]}`, `{fila1[1]}`, `{fila1[2]}`, `{fila1[3]}`, `{fila1[4]}`, `{fila1[5]}`, `{fila1[6]}`, `{fila1[7]}`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, fila)
            conexion.commit()
            print("Tabla de medicamentos restaurada")
    except:
        print("La tabla de datos no ha sido iniciada, vuelva a ejecutar el programa para cargar el guardado")

if confirm:
    cursor.execute("SHOW TABLES")
    a=cursor.fetchall()
    if ('medicamentos', ) not in a:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            fila1=next(lector_csv)
        cursor.execute(f"CREATE TABLE medicamentos (`ID` INT(10) NOT NULL, `{fila1[0]}` VARCHAR(50), `{fila1[1]}` VARCHAR(200), `{fila1[2]}` date, `{fila1[3]}` INT(10), `{fila1[4]}` VARCHAR(25), `{fila1[5]}` INT(3), `{fila1[6]}` DECIMAL(8,2), `{fila1[7]}` VARCHAR(25)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;")
        cursor.execute(f"ALTER TABLE medicamentos ADD PRIMARY KEY (ID), MODIFY ID int(10) NOT NULL AUTO_INCREMENT; COMMIT;")
        conexion.commit()
        print("Creada la tabla de medicamentos")
    tabla_med_upd()
     
