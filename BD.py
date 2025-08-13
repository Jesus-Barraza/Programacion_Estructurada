import mysql.connector
import csv
import funciones

try:
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="db_farmacia",
        use_pure=True
    )
    confirm=True
    print("Conexión exitosa")
    cursor=conexion.cursor(buffered=True)
except mysql.connector.errors.ProgrammingError:
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            use_pure=True
        )
        cursor=conexion.cursor(buffered=True)
    except:
        print(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ...") 
        confirm=False
    else:
        cursor.execute("CREATE DATABASE db_farmacia")
        cursor.execute("USE db_farmacia")
        print("Se creó la base de datos")
        confirm=True
except:
    print(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ...") 
    confirm=False

if confirm:
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS medicamentos (
        ID INT(10) AUTO_INCREMENT PRIMARY KEY, 
        Nombre_marca VARCHAR(50),
        Compuesto_activo VARCHAR(200),
        Caducidad date,
        Concentracion INT(10),
        Presentacion VARCHAR(25),
        Cantidad INT,
        Precio DECIMAL(8,2),
        Laboratorio VARCHAR(25)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
    """)
    conexion.commit()
    print("Se creó la tabla de medicamentos")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id_venta INT AUTO_INCREMENT PRIMARY KEY,
        fecha_venta DATETIME DEFAULT NOW(),
        metodo_pago ENUM('efectivo', 'transferencia') NOT NULL,
        monto_pagado DECIMAL(10,2),
        cambio DECIMAL(10,2)
    );
    """)
    conexion.commit() 
    print("Se creó la tabla de ventas")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detalle_venta (
        id_detalle INT AUTO_INCREMENT PRIMARY KEY,
        id_venta INT NOT NULL,
        id_medicamento INT NOT NULL,
        cantidad INT NOT NULL,
        precio_unitario DECIMAL(10,2) NOT NULL,
        total DECIMAL(10,2) NOT NULL,
        FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
        FOREIGN KEY (id_medicamento) REFERENCES medicamentos(ID)
    );
    """)
    conexion.commit() 
    print("Se creó la tabla de detalles de ventas")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR (50),
        contrasena VARCHAR(65)
    );
    """)
    conexion.commit()
    print("Se creó la tabla de usuarios")
    
def importar_tabla_med():
    funciones.BorrarPantalla()
    print("\n\t\t .:: Importar tabla ::. \n\t\t \u26A0 AVISO \u26A0")
    opc=input(f"Para poder importar los datos de la tabla CSV es importante localizarlo en la carpeta de los archivos \n\n ¿Desea importar la tabla en la base de datos? (si/no): ").capitalize().strip()
    if opc=="Si":
        nom=input("Ingrese el nombre del archivo (procura que no tenga espacios, escribe bien, no agregue el prefijo '.csv'): ").strip() + ".csv"
        try:
            with open(nom, mode='r', encoding='utf-8') as archivo:
                lector_csv = csv.reader(archivo)
                fila1=next(lector_csv)
                nuevos = 0
                for fila in lector_csv:
                    sql = """INSERT INTO medicamentos
                    (Nombre_marca, Compuesto_activo, Caducidad, Concentracion, Presentacion, Cantidad, Precio, Laboratorio)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql, fila)
                    nuevos+=1
            conexion.commit()
            print(f"\n\t\t ::: {nuevos} medicamentos insertados correctamente :::")
        except:
            print("\n\t... Hubo un problema con el programa, inténtalo de nuevo ...")
    else:
        print("\n\t ...Operación abortada con éxito ...")
        
def exportar_tabla_med():
    funciones.BorrarPantalla()
    print("\n\t\t .:: Exportar tabla ::.")
    opc=input(f"La tabla se exportará en un archivo de tipo csv \n\n ¿Desea exportar la tabla en la base de datos? (si/no): ").capitalize().strip() 
    if opc=="Si":
        cursor.execute("SELECT * FROM medicamentos")
        dat=cursor.fetchall()
        nom=input("Ingrese el nombre de la tabla que se exportará: ").lower().strip() + ".csv"
        try:
            with open(nom, mode="w", newline="", encoding="utf-8") as archivo:
                escritor_csv = csv.writer(archivo)
                encabezados = [i[0] for i in cursor.description][1:]
                escritor_csv.writerow(encabezados)
                for fila in dat:
                    escritor_csv.writerow(fila[1:])
                print("\n\t\t :::Tabla de medicamentos exportada:::")
        except:
            print("\n\t... Hubo un problema con el programa, inténtalo de nuevo ...") 
    else:
        print("\n\t ...Operación abortada con éxito ...")

def importar_tabla_ventas():
    funciones.BorrarPantalla()
    print("\n\t\t .:: Importar tabla ::. \n\t\t \u26A0 AVISO \u26A0")
    opc=input(f"Para poder importar los datos de la tabla CSV es importante localizarlo en la carpeta de los archivos \n\n ¿Desea importar la tabla en la base de datos? (si/no): ").capitalize().strip()
    if opc=="Si":
        nom=input("Ingrese el nombre del archivo (procura que no tenga espacios, escribe bien, no agregue el prefijo '.csv'): ").strip() + ".csv"
        try:
            with open(nom, mode='r', encoding='utf-8') as archivo:
                lector_csv = csv.reader(archivo)
                fila1=next(lector_csv)
                nuevos = 0
                for fila in lector_csv:
                    sql = """INSERT INTO ventas
                    (fecha_venta, metodo_pago, monto_pagado, cambio)
                    VALUES (%s, %s, %s, %s)
                    """
                    cursor.execute(sql, fila)
                    nuevos+=1
            conexion.commit()
            print(f"\n\t\t ::: {nuevos} medicamentos insertados correctamente :::")
        except:
            print("\n\t... Hubo un problema con el programa, inténtalo de nuevo ...")
    else:
        print("\n\t ...Operación abortada con éxito ...")
        
def exportar_tabla_ventas():
    funciones.BorrarPantalla()
    print("\n\t\t .:: Exportar tabla ::.")
    opc=input(f"La tabla se exportará en un archivo de tipo csv \n\n ¿Desea exportar la tabla en la base de datos? (si/no): ").capitalize().strip() 
    if opc=="Si":
        cursor.execute("SELECT * FROM ventas")
        dat=cursor.fetchall()
        nom=input("Ingrese el nombre de la tabla que se exportará: ").lower().strip() + ".csv"
        try:
            with open(nom, mode="w", newline="", encoding="utf-8") as archivo:
                escritor_csv = csv.writer(archivo)
                encabezados = [i[0] for i in cursor.description][1:]
                escritor_csv.writerow(encabezados)
                for fila in dat:
                    escritor_csv.writerow(fila[1:])
                print("\n\t\t :::Tabla de medicamentos exportada:::")
        except:
            print("\n\t... Hubo un problema con el programa, inténtalo de nuevo ...") 
    else:
        print("\n\t ...Operación abortada con éxito ...")

def importar_tabla_detven():
    funciones.BorrarPantalla()
    print("\n\t\t .:: Importar tabla ::. \n\t\t \u26A0 AVISO \u26A0")
    opc=input(f"Para poder importar los datos de la tabla CSV es importante localizarlo en la carpeta de los archivos \n\n ¿Desea importar la tabla en la base de datos? (si/no): ").capitalize().strip()
    if opc=="Si":
        nom=input("Ingrese el nombre del archivo (procura que no tenga espacios, escribe bien, no agregue el prefijo '.csv'): ").strip() + ".csv"
        try:
            with open(nom, mode='r', encoding='utf-8') as archivo:
                lector_csv = csv.reader(archivo)
                fila1=next(lector_csv)
                nuevos = 0
                for fila in lector_csv:
                    sql = """INSERT INTO detalle_venta
                    (id_venta, id_medicamento, cantidad, precio_unitario, total)
                    VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql, fila)
                    nuevos+=1
            conexion.commit()
            print(f"\n\t\t ::: {nuevos} medicamentos insertados correctamente :::")
        except:
            print("\n\t... Hubo un problema con el programa, inténtalo de nuevo ...")
    else:
        print("\n\t ...Operación abortada con éxito ...")
        
def exportar_tabla_detven():
    funciones.BorrarPantalla()
    print("\n\t\t .:: Exportar tabla ::.")
    opc=input(f"La tabla se exportará en un archivo de tipo csv \n\n ¿Desea exportar la tabla en la base de datos? (si/no): ").capitalize().strip() 
    if opc=="Si":
        cursor.execute("SELECT * FROM detalle_venta")
        dat=cursor.fetchall()
        nom=input("Ingrese el nombre de la tabla que se exportará: ").lower().strip() + ".csv"
        try:
            with open(nom, mode="w", newline="", encoding="utf-8") as archivo:
                escritor_csv = csv.writer(archivo)
                encabezados = [i[0] for i in cursor.description][1:]
                escritor_csv.writerow(encabezados)
                for fila in dat:
                    escritor_csv.writerow(fila[1:])
                print("\n\t\t :::Tabla de medicamentos exportada:::")
        except:
            print("\n\t... Hubo un problema con el programa, inténtalo de nuevo ...") 
    else:
        print("\n\t ...Operación abortada con éxito ...")
