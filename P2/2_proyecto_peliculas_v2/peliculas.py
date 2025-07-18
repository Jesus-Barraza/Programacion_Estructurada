'''Diccionario de películas para registro de los atributos:
- Nombre
- Categoría
- Clasificación
- Género
- Idioma
'''

#            "nombre":"",
#            "categoria":"",
#            "clasificacion":"",
#            "genero":"",
#            "idioma":""

peliculas={}

#Módulos
def BorrarPantalla():
    import os
    os.system("cls")

def EsperarTecla():
    input("\n\t ---Oprima enter para continuar---")

def AgregarPeliculas():
    BorrarPantalla()
    print("\n\t\t -\|Agregar película|/-")
    peliculas.update({"nombre":input("Ingrese el nombre de la película: ").lower().strip()})
    peliculas.update({"categoria":input("Ingrese la categoría de la película: ").lower().strip()})
    peliculas.update({"clasificacion":input("Ingrese la clasificación de la película: ").upper().strip()})
    peliculas.update({"genero":input("Ingrese el género de la película: ").lower().strip()})
    peliculas.update({"idioma":input("Ingrese el idioma de la película: ").lower().strip()})
    print("\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO! |||")
#o puedes usar pelicula["nombre"]=input("Ingrese la categoría de la película: ").lower().strip()

def MostrarPeliculas():
    BorrarPantalla()
    print("\n\t\t-\|Listas de películas|/-")
    if len(peliculas) > 0:
        for i in peliculas:
            print(f"{i} : {peliculas[i]}")
        print("\n\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO |||")
    else:
        print("\n---La lista se encuentra vacía---\n")

def BorrarPeliculas():
    BorrarPantalla()
    print("\n\t\t-\|Borrar película|/-")
    if len(peliculas) > 0:
        resp="a"
        while resp!="si" and resp!="no":
            resp=input("\n\n\t\t|||CUIDADO|||\n\n¿Desea borrar la película registrada al momento?\n(si/no): ").lower().strip()
            match resp:
                case "si":
                    peliculas.clear()
                    print("\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO! |||")
                case "no":
                    print("\n\t---Se canceló la operación---")
                case _:
                    BorrarPantalla()
                    print("Operación no válida, vuelva a intentarlo")
                    print("\n\t\t-\|Borrar película|/-")
                    resp="a"
    else:
        print("\n---No se puede borrar porque no hay película en el sistema---")

def AgregarCaracteristica():
    BorrarPantalla()
    opc="si"
    print("\n\t\t-\| Agregar características a la película|/-\n")
    while opc=="si":
        cate=input("Ingrese la característica a agregar: ").lower().strip()
        peliculas.update({cate:input(f"Ingrese el valor de la característica {cate}: ").lower().strip()})
        opc="¿Desea agregar alguna otra característica?\n(si/no): " 
    print("\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO! |||")

def ModificarCaracteristica():
    BorrarPantalla()
    print("\n\t\t-\|Modificar características a la película|/-\n")
    if len(peliculas) > 0:
        for i in peliculas:
            print(f"valor actual de {i}: {peliculas[i]}")
            opc=input(f"¿Desea modificar el valor del {i}?\n(si/no): ").lower().strip()
            if opc=="si":
                if i=="clasificacion":
                    peliculas[i]=input(f"Ingrese el nuevo valor del {i}: ").upper().strip()
                else:
                    peliculas[i]=input(f"Ingrese el nuevo valor del {i}: ").lower().strip()
            print("")
        print("\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO! |||")
    else:
        print("\n---No se puede modificar porque no hay película en el sistema---")

def BorrarCaracteristica():
    BorrarPantalla()
    print("\n\t\t -\| Borrar una caracterísitica a la película|/-\n")
    if len(peliculas) > 0:
        print("\tValores actuales:")
        for i in peliculas:
            print(f"{i} : {peliculas[i]}")
        opc=input("\n¿Desea borrar alguna característica? \n(si/no): ").lower().strip()
        match opc:
            case "si":
                cara=input("Ingresa la característica a borrar/quitar: ").lower().strip()
                if cara in peliculas:
                    peliculas.pop(cara)
                    print("\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO! |||")
                else:
                    print("---No se encuentra la característica anterior---")
            case "no":
                print("\n\t---Se canceló la operación---")
            case _:
                print("\n\t---La opción no es correcta, regresando al menú---")
    else:
        print("\n --- No se puede borrar porque no hay película en el sistema---")
