'''Diccionario de películas para registro de los atributos:
- Nombre
- Categoría
- Clasificación
- Género
- Idioma
'''
#Importaciones
import os
try: 
    import mysql.connector
    from mysql.connector import Error
except ModuleNotFoundError:
    os.system("python -m pip install mysql-connector-python")

#Entrada a la base de datos
try:
    mydb = mysql.connector.connect(
    host="::1",
    user="root",
    password="",
    use_pure=True
    )
except Error as e:
    print(f"El error que se presenta es: {e}")

#Base de datos
def BD():
    mycursor=mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    a=f""
    for x in mycursor:
        a+=f"{x}"
    if "('bd_peliculas',)" not in a:
        mycursor.execute("CREATE DATABASE bd_peliculas")
    mycursor.execute("USE bd_peliculas")
    mycursor.execute("SHOW TABLES")
    a=f""
    for x in mycursor:
        a+=f"{x}"
    if "('peliculas',)" not in a:
        mycursor.execute("CREATE TABLE peliculas (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, nombre varchar(100) DEFAULT NULL, categoria varchar(100) DEFAULT NULL, clasificacion varchar(100) DEFAULT NULL, genero varchar(100) DEFAULT NULL, idioma varchar(100) DEFAULT NULL )")


#Módulos
def BorrarPantalla():
    os.system("cls")

def EsperarTecla():
    input("\n\t ---Oprima enter para continuar---")

def AgregarPeliculas():
    mycursor = mydb.cursor()
    BorrarPantalla()
    print("\n\t\t -\|Agregar película|/-")
    nombre=input("Ingrese el nombre de la película: ").lower().strip()
    categoria=input("Ingrese la categoría de la película: ").lower().strip()
    clasificacion=input("Ingrese la clasificación de la película: ").upper().strip()
    genero=input("Ingrese el género de la película: ").lower().strip()
    idioma=input("Ingrese el idioma de la película: ").lower().strip()
    sql = "INSERT INTO peliculas VALUES (%s, %s, %s, %s, %s, %s)"
    val= [None, nombre, categoria, clasificacion, genero, idioma]
    mycursor.execute(sql, val)
    mydb.commit()
    print("\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO! |||")


def MostrarPeliculas():
    mycursor = mydb.cursor()
    BorrarPantalla()
    print("\n\t\t-\|Listas de películas|/-")
    mycursor.execute("SELECT * FROM peliculas")
    myresult = mycursor.fetchall()
    if myresult:
        for x in myresult:
            print(x)
        print("\n\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO |||")
    else:
        print("\n---La lista se encuentra vacía---\n")


def BuscarPeliculas():
    mycursor = mydb.cursor()
    BorrarPantalla()
    print("\n\t\t-\|Buscar películas|/-")
    a=f""
    mycursor.execute("SELECT nombre FROM peliculas")
    for x in mycursor:
        a+=f"{x}"
    print(a)
    if a != "":
        nom=input("Ingrese el nombre de la película a buscar: ").lower().strip()
        var=f"('{nom}',)"
        if var in a:
            sql=("SELECT * FROM peliculas WHERE nombre = %s")
            var=[nom]
            mycursor.execute(sql, var)
            myresult=mycursor.fetchall()
            for x in myresult:
                print(x)
            print("\n\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO |||")
        else:
            print(f"\n---No se encuentra la película {nom}---\n")
    else:
        print("\n---La lista se encuentra vacía---")
            
            
def ModificarPeliculas():
    mycursor = mydb.cursor()
    BorrarPantalla()
    print("\n\t\t -\|Modificar películas|/-\n")
    a=f""
    mycursor.execute("SELECT * FROM peliculas")
    for x in mycursor:
        a+=f"{x}"
    if a != "":
        mycursor.execute("SELECT * FROM peliculas")
        a=f""
        print("\tLista actual:")
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
            a+=f"{x}"
        opc=input("\n¿Desea modificar alguna película? \n(si/no): ").lower().strip()
        match opc:
            case "si":
                nom=input("Ingresa el nombre de la película a modificar: ").lower().strip()
                var=f"'{nom}'"
                if var in a:
                    sql="SELECT * FROM peliculas WHERE nombre = %s"
                    var=(nom, )
                    b=[]
                    mycursor.execute(sql, var)
                    myresult=mycursor.fetchall()
                    for x in myresult:
                        print(x)
                        b.append(x)
                    if len(b) > 1:
                        sql="SELECT id FROM peliculas WHERE nombre = %s"
                        var=(nom, )
                        mycursor.execute(sql, var)    
                        a=""
                        for x in mycursor:
                            a+=f"{x}"
                        print("Hay más de una película")
                        ciclo=True
                        while ciclo:
                            try:
                                id=int(input("Ingrese la ID de la película a modificar (solo números): "))
                                ciclo=False
                            except ValueError:
                                print("Error, ingrese solo números: ")
                        id=f"{id}"
                    else:
                        sql="SELECT id FROM peliculas WHERE nombre = %s"
                        var=(nom, )
                        mycursor.execute(sql, var)
                        myresult = mycursor.fetchall()
                        id=""
                        for x in myresult:
                            for y in x:
                                id = int(y)
                    nomb=input("Ingrese el nuevo nombre: ").lower().strip()
                    cat=input("Ingrese la nueva categoría: ").lower().strip()
                    clas=input("Ingrese la nueva clasificación: ").upper().strip()
                    gen=input("Ingrese el nuevo género: ").lower().strip()
                    idi=input("Ingrese el nuevo idioma: ").lower().strip()
                    muestra=[nomb, cat, clas, gen, idi,]
                    lista=["nombre", "categoria", "clasificacion", "genero", "idioma"]
                    for con in range(0, len(lista)):
                        sql=f"UPDATE peliculas SET {lista[con]} = %s where id = {id}"
                        var=[muestra[con], ]
                        mycursor.execute(sql, var)
                        mydb.commit()
                    print("\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO! |||")
                else:
                    print("\n\t---No se encuentra la película anterior---\n")
            case "no":
                print("\n\t---Se canceló la operación---")
            case _:
                print("\n\t---La opción no es correcta, regresando al menú---")
    else:
        print("\n\t --- No se puede modificar porque no hay película en el sistema---\n")
        
def BorrarPelicula():
    mycursor = mydb.cursor()
    BorrarPantalla()
    print("\n\t\t -\|Borrar película|/-\n")
    a=f""
    mycursor.execute("SELECT * FROM peliculas")
    for x in mycursor:
        a+=f"{x}"
    if a != "":
        mycursor.execute("SELECT nombre FROM peliculas")
        a=f""
        print("\tLista actual:")
        for x in mycursor:
            print(x)
            a+=f"{x}"
        opc=input("\n¿Desea borrar alguna película? \n(si/no): ").lower().strip()
        match opc:
            case "si":
                nom=input("Ingresa el nombre de la película a borrar: ").lower().strip()
                var=f"('{nom}',)"
                if var in a:
                    sql=(f"SELECT * FROM peliculas WHERE nombre = %s")
                    var=[nom]
                    mycursor.execute(sql, var)
                    resultados = mycursor.fetchall()
                    for x in resultados:
                        con=True
                        while con:
                            print("\t\t !Se encontró una película!")
                            opc2=input(f"¿Desea borrar la película {x[1]} de la posición {x[0]}? (si/no): ").lower().strip()
                            match opc2:
                                case "si":
                                    sql=f"DELETE FROM peliculas WHERE id = %s"
                                    var=(x[0], )
                                    mycursor.execute(sql, var)
                                    mydb.commit()
                                    print("\n\t|||Se borró la película con éxito|||\t")
                                    con=False
                                case "no":
                                    con=False
                                case _:
                                    print("Opción incorrecta, vuelva a seleccionar: ")
                else:
                    print("\n\t---No se encuentra la película anterior---\n")
            case "no":
                print("\n\t---Se canceló la operación---")
            case _:
                print("\n\t---La opción no es correcta, regresando al menú---")
    else:
        print("\n---No se puede borrar porque no hay película en el sistema---")
    
def LimpiarPeliculas():
    mycursor = mydb.cursor()
    BorrarPantalla()
    print("\n\t\t-\|Borrar la lista de películas|/-")
    mycursor.execute("USE bd_peliculas")
    a=f""
    mycursor.execute("SELECT * FROM peliculas")
    for x in mycursor:
        a+=f"{x}"
    if a != "":
        resp="a"
        while resp!="si" and resp!="no":
            resp=input("\n\n\t\t|||CUIDADO|||\n\n¿Desea borrar la película registrada al momento?\n(si/no): ").lower().strip()
            match resp:
                case "si":
                    mycursor.execute("DROP TABLE peliculas")
                    BD()
                    print("\n\t|||Se borró la lista con éxito|||\t")
                case "no":
                    print("\n\t---Se canceló la operación---")
                case _:
                    BorrarPantalla()
                    print("Operación no válida, vuelva a intentarlo")
                    print("\n\t\t-\|Borrar película|/-")
                    resp="a"
    else:
        print("\n---No se puede borrar porque no hay película en el sistema---")
