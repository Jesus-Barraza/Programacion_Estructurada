print("Este es main")
import Medicamentos

def main():
    datos = {}
    opcion = ""

    while True:
       Medicamentos.BorrarPantalla()
       opcion = Medicamentos.menu_principal()

       match opcion:
            case "1":
                Medicamentos.AgregarMedicina(datos)
                Medicamentos.EsperarTecla()
            case "2":
                Medicamentos.BorrarMedicina(datos)
                Medicamentos.EsperarTecla()
            case "3":
                Medicamentos.MostrarMedicina(datos)
                Medicamentos.EsperarTecla()
            case "4":
                Medicamentos.BuscarMedicina(datos)
                Medicamentos.EsperarTecla()
            case "5":
                Medicamentos.AcumulacionVentas(datos)
                Medicamentos.EsperarTecla()
            case "6":
                Medicamentos.BorrarPantalla()
                print("\t \U0001F6AA Se ha terminado la ejecución del sistema\n\n\t\t \U0001F389 ::Muchas gracias:: \U0001F389")
                Medicamentos.EsperarTecla()
                break
            case _:
                Medicamentos.BorrarPantalla()
                print("\tOpcion invalida, por favor vuelva a intentarlo\n")
                Medicamentos.EsperarTecla()

if __name__ == "__main__":
    main()
