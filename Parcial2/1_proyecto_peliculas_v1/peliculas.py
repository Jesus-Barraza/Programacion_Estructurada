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
    if len(peliculas) > 0:
        for i in range (0,len(peliculas)):
            print(f"[{i+1}] {peliculas[i]}")
    else:
        print("La lista de películas se encuentra vacía")

def BorrarPeliculas():
    BorrarPantalla()
    print("\n\t -\| Borrar películas |/-\n")
    nomb=input("Ingrese el nombre de la película a borrar: ").lower().strip()
    if nomb not in peliculas:
        print("Esta película no se encuentra en la lista\n\n")
    else:
        cont=0
        pos=0
        while pos < len(peliculas):
            i=peliculas[pos]
            pos+=1
            if i==nomb:
                print("\nSe encontró una película\n")
                resp=input("¿Desea retirar la película? \n (si/no): ").lower().strip()
                if resp=="si":
                    pos-=1
                    print(f"\n Se borró la película{nomb}, el cual estaba en la posición {pos+1}")
                    peliculas.pop(pos)
                    cont+=1
                else:
                    continue
        print(f"\nSe borraron {cont} películas con el título {nomb}")
        print("\n\t |||¡La operación se realizó con éxito!|||")

def ModificarPeliculas():
    BorrarPantalla()
    print("\n\t -\| Modificar películas |/-\n")
    nomb=input("Ingrese el nombre de la película: ").lower().strip()
    if nomb not in peliculas:
        print("Esta película no se encuentra en la lista\n\n")
    else:
        cont=0
        for pos in range(0,len(peliculas)):
            if nomb in peliculas[pos]:
                print("\nSe encontró una película\n")
                opc=input("\n\t¿Desea modificar la película? \n\t\t(si/no):").lower().strip()
                if opc=="si":
                    peliculas[pos]=input("Introduzca el nuevo nombre de la película: ").lower().strip()
                    cont+=1
        print(f"\n\tSe modificaron {cont} películas")
        print("\n\t |||¡La operación se realizó con éxito!|||")



def BuscarPeliculas():
    BorrarPantalla()
    cont=0
    print("\n\t -\| Buscar películas |/-\n")    
    nombre=input("Ingrese el nombre de la película: ").lower().strip()
    if nombre not in peliculas:
        print("Esta película no se encuentra en la lista\n\n")
    else:
        for pos in range(0,len(peliculas)):
            if nombre == peliculas[pos]:
                print(f"En la posición {pos+1} se encuentra la película {nombre}")
                cont+=1
        print(f"\nHay {cont} película(s) con el nombre {nombre}")
    print("\n\t |||¡La operación se realizó con éxito!|||")

def LimpiarPeliculas():
    elec=""
    if elec != ("si" or "no"):
        BorrarPantalla()
        print("\n\t\t -\|Limpiar o borrar todas las listas|/-")
        elec=str(input("\n\t\033[1m |||¡CUIDADO!|||\033[0m\n\n¿Desea limpiar la lista de películas?\n\t(si/no): ")).lower().strip()
        if elec=="si":
            peliculas.clear()
            print("\n\t |||¡La operación se realizó con éxito!|||")
        elif elec=="no":
            print("\n\t |||Se ha cancelado la limpieza de la lista|||")
        else:
            print("\n\t Operación no válida, inténtelo de nuevo")
