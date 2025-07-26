import os
import mysql.connector
import subprocess

os.chdir("F:")
os.chdir("F:/Archivo")
os.chdir("P3")
os.chdir("Inicio base de datos")

mydb = mysql.connector.connect(
host="::1",
user="root",
password="",
use_pure=True
)
mycursor = mydb.cursor()

with open("bd_utd_2a_bis.sql", "r", encoding="utf-8") as archivo_sql:
    script_sql = archivo_sql.read()

# Ejecutar el script SQL
for instruccion in script_sql.split(";"):
    instruccion = instruccion.strip()
    if instruccion:
        try:
            mycursor.execute(instruccion)
        except mysql.connector.Error as err:
            print(f"Error en la instrucción {instruccion}\n{err}")

mydb.commit()
mycursor.close()
mydb.close()
print("Datos importados correctamente.")

def exportar_base_datos(host, usuario, contraseña, nombre_bd, archivo_salida):
    try:
        comando = [
            "mysqldump",
            "-h", host,
            "-u", usuario,
            f"-p", contraseña,
            nombre_bd
        ]
        with open(archivo_salida, "w") as archivo:
            subprocess.run(comando, stdout=archivo, check=True)
        print(f"Base de datos exportada exitosamente a {archivo_salida}")
    except subprocess.CalledProcessError as e:
        print(f"Error al exportar la base de datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        
exportar_base_datos(
    host="::1",
    usuario="root",
    contraseña="",
    nombre_bd="bd_utd_2a_bis",
    archivo_salida="bd_utd_2a_bis.sql"
)