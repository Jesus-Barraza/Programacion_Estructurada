print("Este es main")
import funciones
import BD
from Ventas import ventas
from Usuarios import usuarios
from Medicamentos import Mod
import getpass


def main():
    opcion = True
    while opcion:
       funciones.BorrarPantalla()
       opcion=funciones.menu_usuarios() 
    
       if opcion == "1" or opcion=="RESGISTRO":
            funciones.BorrarPantalla()
            print("\n\t\t .:: Registro en el sistema ::.\n")
            email = input("Ingrese su correo electrónico: ").strip()
            contrasena = getpass.getpass("Ingrese su contraseña: ").strip()
            usuario = usuarios.registrar(email, contrasena)
            if usuario:
                print("\n✅ Su registro fue exitoso.")
                menu_principal()
            else:
                print("\n❌ No fue posible registrar su usuario. Intente de nuevo.")
        
            funciones.EsperarTecla()
       elif opcion == "2" or opcion=="LOGIN":
            funciones.BorrarPantalla()
            print("\n\t\t .:: Inicio de sesion ::.\n")
            email = input("Ingrese su correo electrónico: ").strip().lower()
            contrasena = getpass.getpass("Ingrese su contraseña: ").strip()
            registro = usuarios.iniciar_sesion(email, contrasena)
            if registro:
                 menu_principal()
            else:
                print(f"\n\tCorreo o contraseña incorrectas")
                print("\n\tIntentelo de nuevo")   
            funciones.EsperarTecla()
           
       elif opcion == "3" or opcion=="SALIR":
            print("\nGracias por usar el sistema. Hasta pronto.")
            opcion=False
            funciones.EsperarTecla()  
       else:
            print("Opcion no valida")
            opcion=True
            funciones.EsperarTecla() 

def menu_principal():
    while True:
        funciones.BorrarPantalla()
        print("\n\t\t .:: Menú Principal ::.\n")
        print("1. Menú de venta")
        print("2. Menú de medicamentos")
        print("3. Exportar tabla de medicamentos")
        print("4. Importar tabla de medicamentos")
        print("5. Exportar ventas")
        print("6. Importar ventas")
        print("7. Exportar detalle de ventas")
        print("8. Importar detalle de ventas")
        print("9. Salir al menú de inicio")
    
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            funciones.BorrarPantalla()
            ventas.menu_ventas()
        elif opcion == "2":
            funciones.BorrarPantalla()
            menu_medicamentos()
        elif opcion == "3":
            funciones.BorrarPantalla()
            BD.exportar_tabla_med()
            funciones.EsperarTecla()
        elif opcion == "4":
            funciones.BorrarPantalla()
            BD.importar_tabla_med()
            funciones.EsperarTecla()
        elif opcion == "5":
            funciones.BorrarPantalla()
            BD.exportar_tabla_ventas()
            funciones.EsperarTecla()
        elif opcion == "6":
            funciones.BorrarPantalla()
            BD.importar_tabla_ventas()
            funciones.EsperarTecla()
        elif opcion == "7":
            funciones.BorrarPantalla()
            BD.exportar_tabla_detven()
            funciones.EsperarTecla()
        elif opcion == "8":
            funciones.BorrarPantalla()
            BD.importar_tabla_detven()
            funciones.EsperarTecla()
        elif opcion == "9":
            funciones.BorrarPantalla()
            print("\n🔙 Regresando al menú de inicio...")
            funciones.EsperarTecla()
            break
        else:
            print("\n⚠️ Opción inválida. Intente de nuevo.")

def menu_medicamentos():
    opcion = ""

    while True:
        funciones.BorrarPantalla()
        opcion = funciones.menu_inventario()

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
                Mod.ModificarMedicina()
                funciones.EsperarTecla()
            case "7":
                funciones.BorrarPantalla()
                print("\t \U0001F6AA ...Regresando al menú de inicio...")
                funciones.EsperarTecla()
                menu_principal()
            case _:
                funciones.BorrarPantalla()
                print("\tOpcion invalida, por favor vuelva a intentarlo\n")
                funciones.EsperarTecla()

if __name__ == "__main__":
    main()