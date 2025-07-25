'''Base a utilizar:
pos0: nombre
pos1: calificación 1
pos2: calificación 2
pos3: calificación 3
'''

#Importaciones
import calificaciones

#Función
def main():
    #Iniciador
    opc=True
    
    #Base de datos
    calificaciones.BD()

    #Menú
    calificaciones.BorrarPantalla()
    while opc:
        opc=calificaciones.Menu()
        match opc:
            case "1":
                calificaciones.AgregarCalificaciones("calificaciones")
                calificaciones.EsperarTecla()
            case "2":
                calificaciones.MostrarCalificaciones("calificaciones")
                calificaciones.EsperarTecla()
            case "3":
                calificaciones.PromediarCalificaciones("calificaciones")
                calificaciones.EsperarTecla()
            case "4":
                calificaciones.BuscarCalificaciones("calificaciones")
                calificaciones.EsperarTecla()
            case "5":
                calificaciones.BorrarPantalla()
                print("\t--- 🚪Se ha terminado la ejecución del sistema🚪 --- \n\n\t\t ||| 🎉MUCHAS GRACIAS🎉 |||")
                calificaciones.EsperarTecla()
                opc=False
            case _:
                calificaciones.BorrarPantalla()
                print("\t--- ❌Entrada no válida, vuelva a intentar❌ ---\n")
                opc=True

if __name__ == "__main__":
    main()