import mysql.connector
import csv
import funciones
ruta="F:/Archivo/PF/"

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
    funciones.BorrarPantalla()
    print("\n\t\t .:: Importar tabla ::. \n\t\t \u26A0 AVISO \u26A0")
    opc=input(f"Para poder importar los datos de la tabla CSV es importante localizarlo en la carpeta 'PF' del directorio {ruta} \n\n ¿Desea importar la tabla en la base de datos? (si/no): ").capitalize().strip()
    if opc=="Si":
        nom=input("Ingrese el nombre del archivo (procura que no tenga espacios, escribe bien, no agregue el prefijo '.csv'): ").strip() + ".csv"
        try:
            with open(ruta+nom, mode='r', encoding='utf-8') as archivo:
                lector_csv = csv.reader(archivo)
                fila1=next(lector_csv)
                for fila in lector_csv:
                    sql = f"INSERT INTO medicamentos (`{fila1[0]}`, `{fila1[1]}`, `{fila1[2]}`, `{fila1[3]}`, `{fila1[4]}`, `{fila1[5]}`, `{fila1[6]}`, `{fila1[7]}`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, fila)
            conexion.commit()
            print("\n\t\t :::Tabla de medicamentos importada:::")
        except:
            print("\n\t... Hubo un problema con el programa, inténtalo de nuevo ...")
    else:
        print("\n\t ...Operación abortada con éxito ...")
        
def exportar_tabla_med():
    funciones.BorrarPantalla()
    print("\n\t\t .:: Exportar tabla ::.")
    opc=input(f"La tabla se exportará en un archivo csv en {ruta} \n\n ¿Desea exportar la tabla en la base de datos? (si/no): ").capitalize().strip() 
    if opc=="Si":
        cursor.execute("SELECT * FROM medicamentos")
        dat=cursor.fetchall()
        nom=input("Ingrese el nombre de la tabla que se exportará: ").lower().strip() + ".csv"
        try:
            with open(nom, mode="w", newline="", encoding="utf-8") as archivo:
                escritor_csv = csv.writer(archivo)
                encabezados = [i[0] for i in cursor.description]
                escritor_csv.writerow(encabezados)
                escritor_csv.writerows(dat)
                print("\n\t\t :::Tabla de medicamentos exportada:::")
        except:
            print("\n\t... Hubo un problema con el programa, inténtalo de nuevo ...") 
    else:
        print("\n\t ...Operación abortada con éxito ...")

def crear_tab_med():
    if confirm:
        cursor.execute("SHOW TABLES")
        a=cursor.fetchall()
        if ('medicamentos', ) not in a:
            cursor.execute(f"CREATE TABLE medicamentos (`ID` INT(10) NOT NULL, `nombre de la marca` VARCHAR(50), `nombre del compuesto activo` VARCHAR(200), `caducidad` date, `ml/mg` INT(10), `presentacion` VARCHAR(25), `cantidad` INT(3), `precio al publico` DECIMAL(8,2), `laboratorio` VARCHAR(25)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;")
            cursor.execute(f"ALTER TABLE medicamentos ADD PRIMARY KEY (ID), MODIFY ID int(10) NOT NULL AUTO_INCREMENT; COMMIT;")
            conexion.commit()
            print("Creada la tabla de medicamentos")