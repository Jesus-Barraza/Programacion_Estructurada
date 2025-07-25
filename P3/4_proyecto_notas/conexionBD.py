import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_notas",
        use_pure=True
    )
    cursor=conexion.cursor(buffered=True)
except:
    print(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ...") 


