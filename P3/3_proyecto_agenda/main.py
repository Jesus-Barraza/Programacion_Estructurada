#Importaciones
import agenda

#Función
def main():
    #Iniciador
    opc=True

    #Datos de inicio
    agenda.BD()
    agenda.BorrarPantalla()
    
    #Menú
    while opc:
        accion = agenda.TablaApropiada()
        opc=agenda.Menu()
        match opc:
            case "1":
                agenda.AgregarContacto(accion)
                agenda.EsperarTecla()
                agenda.BorrarPantalla()
            case "2":
                agenda.MostrarContacto(accion)
                agenda.EsperarTecla()
                agenda.BorrarPantalla()
            case "3":
                agenda.BuscarContacto(accion)
                agenda.EsperarTecla()
                agenda.BorrarPantalla()
            case "4":
                agenda.BorrarContacto(accion)
                agenda.EsperarTecla()
                agenda.BorrarPantalla()
            case "5":
                agenda.ModificarContacto(accion)
                agenda.EsperarTecla()
                agenda.BorrarPantalla()
            case "6":
                agenda.BorrarPantalla()
                print("\t\U0001F6AA ---Se ha terminado la ejecución del sistema--- \U0001F6AA \n\n\t\t\U0001F389 |||MUCHAS GRACIAS||| \U0001F389")
                agenda.EsperarTecla()
                opc=False
            case _:
                agenda.BorrarPantalla()
                print("\t\u274C ---Entrada no válida, vuelva a intentar--- \u274C\n")
                opc=True

if __name__ == "__main__":
    main()
