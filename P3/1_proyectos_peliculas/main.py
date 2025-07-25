'''
Crear un proyecto que permita gestionar (administrar) películas. Colocar un menú de opciones:
Agregar, Borrar, Modificar, Mostrar, Buscar, Limpar una lista de películas.

Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar diccionarios para almacenas los atributos (nombre, categoría, clasificación, género e idioma) de películas
3.- Implementar y utilizar una BD relacional en MySQL
'''

#Importaciones
import peliculas
opcion=True

#Menú
peliculas.BD()
peliculas.BorrarPantalla()
while opcion:
    print("\n\t\t\t -\| GESTIÓN DE PELÍCULAS |/- \n\n\t 1.- Agregar película \n\t 2.- Mostrar películas \n\t 3.- Buscar películas \n\t 4.- Modificar película \n\t 5.- Borrar película \n\t 6.- Borrar la lista \n\t 7.- Salir")
    opcion=str(input("\n\t\t Elige una opción \n\t(1/2/3/4/5/6/7):")).lower().strip()

    match opcion:
        case "1":
            peliculas.AgregarPeliculas()
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "2":
            peliculas.MostrarPeliculas()            
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "3":
            peliculas.BuscarPeliculas()
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "4":
            peliculas.ModificarPeliculas()
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "5":
            peliculas.BorrarPelicula()
            peliculas.EsperarTecla()
            peliculas.BorrarPantalla()
        case "6":
            peliculas.LimpiarPeliculas()
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
