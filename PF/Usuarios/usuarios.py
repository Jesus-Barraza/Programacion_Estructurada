
import datetime
import hashlib
from BD import *
def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        cursor.execute(
            "INSERT INTO usuarios (id_usuario,  email, contrasena) VALUES (NULL,%s, %s)", (email, contrasena)
        )
        conexion.commit()
        return True
    except:
        print("Error al registrar") 
        return False
           

def iniciar_sesion(email,contrasena):
    try:
        contrasena=hash_password(contrasena)
        cursor.execute(
            "select * from usuarios where email=%s and contrasena=%s", (email, contrasena)
        )
        registros=cursor.fetchone()
        if registros:
            return registros
        else:
            return None
    except:
        print("Error iniciar sesion")
        return None
         
