#Importaciones
import os

#Funciones
def BorrarPantalla():
    os.system("cls")

def EsperarTecla():
    input("\n\t --- Pulse enter para continuar ---")
    BorrarPantalla()

def Menu():
    print("\t\t -\| Sistema de Gestión de Calificaciones |/-")
    op=input("\n\tElige una opción \n1.- Agregar \n2.- Mostrar \n3.- Calcular promedios \n4.- SALIR \n (1-4): ")
    return op

def AgregarCalificaciones(dat):
    BorrarPantalla()
    print("\t\t-\| Agregar Calificaciones |/-\n")
    nom=input("Ingrese el nombre del alumno: ").capitalize().strip()
    cali=[]
    for i in range(1,4):
        ver=True
        while ver:
            try: 
                cal=round(float(input(f"Ingrese la calificación número {i}: ")), 1)
                if cal>=0 and cal <=10:
                    cali.append(cal)
                    ver=False
                else:
                    print("---❌ Ingrese un valor comprendido entre el 0 y el 10 ❌---\n")
            except ValueError:
                print("\t---❌ La calificación es un valor numérico ❌---\n") 
    dat.append([nom]+cali)
    print("\n\t\t||| La operación se realizó con éxito |||")

def MostrarCalificaciones(dat):
    BorrarPantalla()
    print("\t\t-\| Mostrar las calificaciones |/-\n")
    if len(dat)>0:
        i=len(dat)
        print(f"{'Nombre':<15} | {'Cal. 1':<10} | {'Cal. 2':<10} | {'Cal. 3':<10}")
        print(f"{'_'*60}")
        for col in dat:
            print(f"{col[0]:<15}   {col[1]:<10}   {col[2]:<10}   {col[3]:<10}")
        print(f"{'_'*60}")
        print(f"\nHay un total de {i} alumnos registrados\n")
    else:
        print("--- No hay calificaciones en el sistema ---")

def PromediarCalificaciones(dat):
    BorrarPantalla()
    print("\t\t-\| Promedios |/-\n")
    if len(dat)>0:
        sum=0
        i=len(dat)
        print(f"{'Nombre':<15} | {'Promedio':<10}")
        print(f"{'_'*40}")
        for col in dat:
            nom=col[0]
            prom=(col[1]+col[2]+col[3])/(len(col)-1)
            print(f"{nom:<15}   {prom:.2f}")
            sum+=prom
        print(f"{'_'*40}")
        prom_grup=sum/len(dat)
        print(f"\nHay un total de {i} alumnos registrados y el promedio grupal es de {prom_grup}\n")
    else:
        print("--- No hay calificaciones en el sistema ---")
#Tambien puedes usar prom=sum(col[1:]/len(col)-1)