'''
Crear un proyecto que permita gestionar (administrar) películas. Colocar un menú de opciones:
Agregar, Borrar, Modificar, Mostrar, Buscar, Limpar una lista de películas.

Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar diccionarios para almacenas los atributos (nombre, categoría, clasificación, género e idioma) de películas

'''

#Importaciones
import peliculas
opcion=True

#Menú
peliculas.BorrarPantalla()
while opcion:
    print("\n\t\t\t -\| GESTIÓN DE PELÍCULAS |/- \n\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Mostrar \n\t 4.- Agregar característica \n\t 5.- Modificar característica \n\t 6.- Borrar característica \n\t 7.- Salir")
    opcion=str(input("\n\t\t Elige una opción \n\t(1/2/3/4/5/6/7):")).lower().strip()

    match opcion:
        case "1":
            peliculas.AgregarPeliculas()
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "2":
            peliculas.BorrarPeliculas()
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "3":
            peliculas.MostrarPeliculas()
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "4":
            peliculas.AgregarCaracteristica()
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "5":
            peliculas.ModificarCaracteristica()
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "6":
            peliculas.BorrarCaracteristica()
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "7":
            peliculas.BorrarPantalla()
            print("\n\tTerminaste la ejecución del sistema \n\t\t -\|Gracias|/-")
            opcion=False
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case _:
            peliculas.BorrarPantalla()
            print("\n\tOpción inválida, vuelva a intentarlo")
            opcion=True
