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
    print("\n\t -\|Agregar película|/-")
    peliculas.update(input("Ingrese el nombre de la película: ").upper().strip())
    atributo=input("Ingresa la característica a añadir: ").lower().append()
    valor_atributo=input("Ingresa el valor de la característica: ").lower().append()

#def MostrarPeliculas():

#def BorrarPeliculas():

#def AgregarCaracteristica():

#def ModificarCaracteristica():

#def BorrarCaracteristica():
