#Lista de películas para registro
peliculas=["toy", "vengador", "toy", "toy"]

def BorrarPantalla():
    import os
    os.system("cls")

#intento 1
#def BorrarPeliculas():
#    BorrarPantalla()
#    print("\n\t -\| Borrar películas |/-\n")
#    nomb=input("Ingrese el nombre de la película a borrar: ").lower().strip()
#    if nomb not in peliculas:
#        print("Esta película no se encuentra en la lista\n\n")
#    else:
#        cont=0
#        for i in peliculas:
#            if nomb==i:
#                print("\nSe encontró una película\n")
#                resp=input("¿Desea retirar la película? \n (si/no): ").lower().strip()
#                if resp=="si":
#                    pos=peliculas.index(i)
#                    print(f"\n Se borró la película {nomb}, el cual estaba en la posición {pos+1}")
#                    peliculas.pop(pos)
#                    i=peliculas[0]
#                    cont+=1
#                else:
#                    i=peliculas[peliculas.index(i)+1]
#        print(f"\nSe borraron {cont} películas con el título {nomb}")
#        print("\n\t |||¡La operación se realizó con éxito!|||")

#intento 2
#def BorrarPeliculas():
#    BorrarPantalla()
#    print("\n\t -\| Borrar películas |/-\n")
#    nomb=input("Ingrese el nombre de la película a borrar: ").lower().strip()
#    if nomb not in peliculas:
#        print("Esta película no se encuentra en la lista\n\n")
#    else:
#        cont=0
#        pos=-1
#        for i in peliculas:
#            pos+=1
#            if nomb==i:
#                print("\nSe encontró una película\n")
#                resp=input("¿Desea retirar la película? \n (si/no): ").lower().strip()
#                if resp=="si":
#                    print(f"\n Se borró la película{nomb}, el cual estaba en la posición {pos+1}")
#                    peliculas.pop(pos)
#                    i=peliculas[pos]
#                    cont+=1
#                    pos-=1
#                else:
#                    i=peliculas[pos+1]
#        print(f"\nSe borraron {cont} películas con el título {nomb}")
#        print("\n\t |||¡La operación se realizó con éxito!|||")

#Intento 3
def BorrarPeliculas():
    BorrarPantalla()
    print("\n\t -\| Borrar películas |/-\n")
    nomb=input("Ingrese el nombre de la película a borrar: ").lower().strip()
    if nomb not in peliculas:
        print("Esta película no se encuentra en la lista\n\n")
    else:

BorrarPeliculas()