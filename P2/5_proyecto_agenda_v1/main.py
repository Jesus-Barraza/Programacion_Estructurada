#Importaciones
import agenda

#Función
def main():
    #Iniciador
    opc=True

    #Base
    dict={}

    #Menú
    while opc:
        agenda.BorrarPantalla()
        opc=agenda.Menu()
        match opc:
            case "1":
                agenda.AgregarContacto(dict)
                agenda.EsperarTecla()
            case "2":
                agenda.MostrarContacto(dict)
                agenda.EsperarTecla()
            case "3":
                agenda.BuscarContacto(dict)
                agenda.EsperarTecla()
            case "4":
                agenda.BorrarContacto(dict)
                agenda.EsperarTecla()
            case "5":
                agenda.ModificarContacto(dict)
                agenda.EsperarTecla()
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