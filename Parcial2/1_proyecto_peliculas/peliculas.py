#Lista de películas para registro
peliculas=[]

#Módulos
def BorrarPantalla():
    import os
    os.system("cls")

def EsperarTecla():
    input("\n\t ---Oprima enter para continuar---")

def AgregarPeliculas():
    BorrarPantalla()
    print("\n\t -\| Agregar películas |/-\n")
    peliculas.append(input("Ingrese el nombre de la película: ").lower().strip())
    print("\n\t |||¡La operación se realizó con éxito!|||")

def MostrarPeliculas():
    BorrarPantalla()
    print("\n\t\t -\| Lista de películas |/-\n")
    for i in range (0,len(peliculas)):
        print(f"[{i+1}] {peliculas[i]}")

def BorrarPeliculas():
    BorrarPantalla()
    errorDet=True
    while errorDet:
        try:
            print("\n\t -\| Borrar películas |/-\n")
            peliculas.remove(input("Ingrese el nombre de la película a borrar: ").lower().strip())
        except ValueError:
            BorrarPantalla()
            print("Esta película no se encuentra en la lista, inténtelo de nuevo\n\n")
        else:
            errorDet=False
            print("\n\t |||¡La operación se realizó con éxito!|||")

def ModificarPeliculas():
    BorrarPantalla()
    errorDet=True
    while errorDet:
        try:
            print("\n\t -\| Modificar películas |/-\n")
            posicion=peliculas.index(input("Ingrese el nombre de la película: ").lower().strip())
        except ValueError:
            BorrarPantalla()
            print("Esta película no se encuentra en la lista, inténtelo de nuevo\n\n")
        else:
            errorDet=False
    peliculas[posicion]=input("Ingrese de qué manera desea modificarlo: ")
    print("\n\t |||¡La operación se realizó con éxito!|||")

def BuscarPeliculas():
    BorrarPantalla()
    errorDet=True
    while errorDet:
        try:
            print("\n\t -\| Buscar películas |/-\n")
            nombre=input("Ingrese el nombre de la película: ").lower().strip()
            posicion=peliculas.index(nombre)
        except ValueError:
            BorrarPantalla()
            print("Esta película no se encuentra en la lista, inténtelo de nuevo\n\n")
        else:
            errorDet=False
            print(f"\n En la posición {posicion} se encuentra la película {nombre}")
    print("\n\t |||¡La operación se realizó con éxito!|||")

def LimpiarPeliculas():
    BorrarPantalla()
    eleccion=""
    while eleccion=="":
        eleccion=input("\n\t\033[1m |||¡CUIDADO!|||\033[0m\n\n¿Desea limpiar la lista de películas?\n\t(s/n): ").lower().strip()
        if eleccion=="s":
            peliculas.clear()
            print("\n\t |||¡La operación se realizó con éxito!|||")
        else:
            print("\n\t |||Se ha cancelado la limpieza de la lista|||")
