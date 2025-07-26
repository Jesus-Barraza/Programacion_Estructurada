from conexionBD import *

def crear_nota(id, h1, desc):
    try:
        cursor.execute("INSERT INTO notas (usuario_id, titulo, descripcion, fecha) VALUES (%s, %s, %s, NOW())",(id, h1, desc))
        conexion.commit()
        return True
    except:
        return False
    
'''También puede ser:
import datetime
date=datetime.datetime.now()
cursor.execute("INSERT INTO notas (usuario_id, titulo, descripcion, fecha) VALUES (%s, %s, %s, %s)",(id, h1, desc, date))
'''

def mostrar_nota(uid):
    try:
        cursor.execute("SELECT * FROM notas WHERE usuario_id = %s", (uid,))
        return cursor.fetchone()
    except:
        return []

'''También se puede usar:
reg=cursor.fetchall()
if len(reg) > 0:
    return reg
else:
    return []
'''

def cambiar_notas(id,h1,desc):
    try:
        cursor.execute("UPDATE FROM notas SET titulo = %s, descripcion = %s, fecha = NOW() WHERE id = %s",(h1, desc, id))
        conexion.commit()
        return True
    except:
        return False
    
def borrar_notas(id):
    try:
        cursor.execute("DELETE FROM notas WHERE id = %s",(id, ))
        conexion.commit()
        return True
    except:
        return False

def buscar_nota(id):
    try:
        cursor.execute("SELECT * FROM notas WHERE id = %s", (id))
        return cursor.fetchone()
    except:
        return []