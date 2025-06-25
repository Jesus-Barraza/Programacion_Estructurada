#Importaciones
import calificaciones

#Iniciador
entrace=True

#Menú
calificaciones.BorrarPantalla()
while entrace:
    print("\t\t -\| Sistema de Gestión de Calificaciones |/-")
    entrace=input("\n\tElige una opción \n1.- Agregar \n2.- Mostrar \n3.- Calcular promedios \n4.- SALIR \n (1-4): ")
    match entrace:
        case "1":
            calificaciones.BorrarPantalla()
            calificaciones.AgregarCalificaciones()
            calificaciones.EsperarTecla()
        case "2":
            calificaciones.BorrarPantalla()
            calificaciones.MostrarCalificaciones()
            calificaciones.EsperarTecla()
        case "3":
            calificaciones.BorrarPantalla()
            calificaciones.PromediarCalificaciones()
            calificaciones.EsperarTecla()
        case "4":
            calificaciones.BorrarPantalla()
            print("\t--- Se ha terminado la ejecución del sistema --- \n\n\t\t ||| MUCHAS GRACIAS |||")
            calificaciones.EsperarTecla()
            entrace=False
        case _:
            calificaciones.BorrarPantalla()
            print("\t--- ❌Entrada no válida, vuelva a intentar❌ ---\n")
