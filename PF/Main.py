print("Este es main")
from Medicamentos import Mod
import funciones
import BD


def main():
    opcion = ""

    while True:
        funciones.BorrarPantalla()
        opcion = funciones.menu_principal()

        match opcion:
            case "1":
                Mod.AgregarMedicina()
                funciones.EsperarTecla()
            case "2":
                Mod.BorrarMedicina()
                funciones.EsperarTecla()
            case "3":
                Mod.MostrarMedicina()
                funciones.EsperarTecla()
            case "4":
                Mod.BuscarMedicina()
                funciones.EsperarTecla()
            case "5":
                Mod.FechaCaducidad()
                funciones.EsperarTecla()
            case "6":
                funciones.BorrarPantalla()
                print("\t \U0001F6AA Se ha terminado la ejecución del sistema\n\n\t\t \U0001F389 ::Muchas gracias:: \U0001F389")
                funciones.EsperarTecla()
                break
            case "7":
                Mod.ModificarMedicina()
                funciones.EsperarTecla()
            case "8":
                BD.tabla_med_upd()
                funciones.EsperarTecla()
            case "9":
                BD.exportar_tabla_med()
                funciones.EsperarTecla()
            case _:
                funciones.BorrarPantalla()
                print("\tOpcion invalida, por favor vuelva a intentarlo\n")
                funciones.EsperarTecla()

if __name__ == "__main__":
    main()
