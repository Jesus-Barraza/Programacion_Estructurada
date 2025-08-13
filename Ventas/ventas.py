from BD import *
import funciones
print("se importo funciones")
import datetime
from decimal import Decimal


    
def medicamentos_stock(): #Esta funcion le permite al vendedor ver la lista de todos los medicamentos disponibles
    cursor.execute("SELECT ID, Nombre_marca, Precio, Cantidad FROM medicamentos;")
    medicamentos = cursor.fetchall()
    return medicamentos
meds = medicamentos_stock()
print(f"Medicamentos en existencia: {len(meds)}")
for med in meds:
    print(f"{'ID':<10}{'Nombre':<15}{'Precio':<15}{'Cantidad':<15}")
    print(f"-"*60)
    print(f"{med[0]:<10} {med[1]:<15}{med[2]:<15}{med[3]:<15}")
    print(f"-"*60)

def buscar_medicamento(): #Esta funcion permite la busqueda del medicamento por nombre
      nombre=input("Dame el nombre del medicamento a buscar: ").upper().strip()
      sql="select id, nombre_marca, precio, cantidad from medicamentos where nombre_marca=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      coincidencia=cursor.fetchall()
      if coincidencia:
        print(f"\n\tMostrar los medicamentos")
        print(f"-"*80)
        for med in coincidencia:
          print(f"{'ID':<10}{'Nombre':<15}{'Precio':<15}{'Cantidad':<15}")
          print(f"-"*60)
          print(f"{med[0]:<10}{med[1]:<15}{med[2]:<15}{med[3]:<15}")
          print(f"-"*60)
      else:
        print("\n\t .:: No hay medicamentos que coincidan con ese nombre::. ")    


lista_medicamentos = [
    {"id_medicamento": 1, "cantidad": 2},
    {"id_medicamento": 5, "cantidad": 1},
]

def registrar_venta(metodo_pago, monto_pagado, lista_medicamentos):
    try:
        total = 0
        detalles = []

        # Calcular total y preparar detalles
        for item in lista_medicamentos:
            cursor.execute("SELECT precio, cantidad FROM medicamentos WHERE id = %s", (item["id_medicamento"],))
            resultado = cursor.fetchone()
            if not resultado:
                print(f"Medicamento ID {item['id_medicamento']} no encontrado.")
                return False
            precio_unitario, stock = resultado
            if item["cantidad"] > stock:
                print(f"Stock insuficiente para medicamento ID {item['id_medicamento']}.")
                return False
            subtotal = precio_unitario * item["cantidad"]
            total += subtotal
            detalles.append({
                "id_medicamento": item["id_medicamento"],
                "cantidad": item["cantidad"],
                "precio_unitario": precio_unitario,
                "subtotal": subtotal
            })

        # Validar pago
        if monto_pagado < total:
            print("Monto pagado insuficiente.")
            return False
        cambio = monto_pagado - total

        # Insertar en ventas
        cursor.execute("""
            INSERT INTO ventas (fecha_venta, metodo_pago, monto_pagado, cambio)
            VALUES (NOW(), %s, %s, %s)
        """, (metodo_pago, monto_pagado, cambio))
        id_venta = cursor.lastrowid

        # Insertar en detalle_venta y actualizar inventario
        for detalle in detalles:
            cursor.execute("""
                INSERT INTO detalle_venta (id_venta, id_medicamento, cantidad, precio_unitario, subtotal)
                VALUES (%s, %s, %s, %s, %s)
            """, (id_venta, detalle["id_medicamento"], detalle["cantidad"], detalle["precio_unitario"], detalle["subtotal"]))

            cursor.execute("""
                UPDATE medicamentos SET cantidad = cantidad - %s WHERE id = %s
            """, (detalle["cantidad"], detalle["id_medicamento"]))

        conexion.commit()
        print(f"Venta registrada exitosamente. ID venta: {id_venta}, Cambio: ${cambio:.2f}")
        return True

    except Exception as e:
        conexion.rollback()
        print("Error al registrar la venta1:", e)
        return False


def capturar_venta():
    lista_medicamentos = []
    metodos_validos = ["efectivo", "tarjeta"]
    metodo_pago = ""
    while metodo_pago not in metodos_validos:
        metodo_pago = input("Método de pago (efectivo/tarjeta): ").strip().lower()

    monto_pagado_input = float(input("Monto pagado por el cliente: "))
    Decimal(monto_pagado_input)
    

    while True:
        try:
            id_medicamento = int(input("ID del medicamento: "))
            cantidad = int(input("Cantidad: "))
            lista_medicamentos.append({"id_medicamento": id_medicamento, "cantidad": cantidad})
        except ValueError:
            print("Entrada inválida.")
            continue

        continuar = input("¿Agregar otro medicamento? (s/n): ").strip().lower()
        if continuar != 's':
            break

    registrar_venta(metodo_pago, monto_pagado_input, lista_medicamentos)

def generar_recibo(id_venta, detalles, total, monto_pagado, cambio):
    print("\n=== Recibo de Venta ===")
    print(f"ID de Venta: {id_venta}")
    print(f"{'ID Medicamento':<15}{'Cantidad':<10}{'Precio':<10}{'Subtotal':<10}")
    print("-" * 50)
    for detalle in detalles:
        print(f"{detalle['id_medicamento']:<15}{detalle['cantidad']:<10}{detalle['precio_unitario']:<10.2f}{detalle['subtotal']:<10.2f}")
    print("-" * 50)
    print(f"Total: ${total:.2f}")
    print(f"Monto pagado: ${monto_pagado:.2f}")
    print(f"Cambio: ${cambio:.2f}")
    print("=" * 50)

def menu_ventas():
    opcion = ""
    while opcion != "4":
        print("\n=== Menú de Ventas ===")
        print("1. Buscar medicamento por nombre")
        print("2. Capturar venta y generar ticket")
        print("3. Ver medicamentos en stock")
        print("4. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            funciones.BorrarPantalla()
            buscar_medicamento()
            funciones.EsperarTecla()

        elif opcion == "2":
            funciones.BorrarPantalla()
            lista_medicamentos = []
            metodos_validos = ["efectivo", "tarjeta"]
            metodo_pago = ""
            while metodo_pago not in metodos_validos:
                metodo_pago = input("Método de pago (efectivo/tarjeta): ").strip().lower()

            try:
                monto_pagado_input = float(input("Monto pagado por el cliente: "))
                monto_pagado = Decimal(monto_pagado_input)
            except ValueError:
                print("Monto inválido.")
                continue

            while True:
                try:
                    id_medicamento = int(input("ID del medicamento: "))
                    cantidad = int(input("Cantidad: "))
                    lista_medicamentos.append({"id_medicamento": id_medicamento, "cantidad": cantidad})
                except ValueError:
                    print("Entrada inválida.")
                    continue

                continuar = input("¿Agregar otro medicamento? (s/n): ").strip().lower()
                if continuar != 's':
                    break

            try:
                total = 0
                detalles = []

                for item in lista_medicamentos:
                    cursor.execute("SELECT precio, cantidad FROM medicamentos WHERE id = %s", (item["id_medicamento"],))
                    resultado = cursor.fetchone()
                    if not resultado:
                        print(f"Medicamento ID {item['id_medicamento']} no encontrado.")
                        break
                    precio_unitario, stock = resultado
                    if item["cantidad"] > stock:
                        print(f"Stock insuficiente para medicamento ID {item['id_medicamento']}.")
                        break
                    subtotal = precio_unitario * item["cantidad"]
                    total += subtotal
                    detalles.append({
                        "id_medicamento": item["id_medicamento"],
                        "cantidad": item["cantidad"],
                        "precio_unitario": precio_unitario,
                        "subtotal": subtotal
                    })

                if monto_pagado < total:
                    print("Monto pagado insuficiente.")
                    continue

                cambio = monto_pagado - total

                cursor.execute("""
                    INSERT INTO ventas (fecha_venta, metodo_pago, monto_pagado, cambio)
                    VALUES (NOW(), %s, %s, %s)
                """, (metodo_pago, monto_pagado, cambio))
                id_venta = cursor.lastrowid

                for detalle in detalles:
                    cursor.execute("""
                        INSERT INTO detalle_venta (id_venta, id_medicamento, cantidad, precio_unitario, total)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (id_venta, detalle["id_medicamento"], detalle["cantidad"], detalle["precio_unitario"], detalle["subtotal"]))

                    cursor.execute("""
                        UPDATE medicamentos SET cantidad = cantidad - %s WHERE id = %s
                    """, (detalle["cantidad"], detalle["id_medicamento"]))

                conexion.commit()
                print(f"\n✅ Venta registrada exitosamente. ID venta: {id_venta}")
                generar_recibo(id_venta, detalles, total, monto_pagado, cambio)

            except Exception as e:
                conexion.rollback()
                print("Error al registrar la venta:", e)
            funciones.EsperarTecla()

        elif opcion == "3":
            funciones.BorrarPantalla()
            meds = medicamentos_stock()
            print(f"\nMedicamentos en existencia: {len(meds)}")
            print(f"{'ID':<10}{'Nombre':<15}{'Precio':<15}{'Cantidad':<15}")
            print("-" * 60)
            for med in meds:
                print(f"{med[0]:<10}{med[1]:<15}{med[2]:<15}{med[3]:<15}")
            print("-" * 60)
            funciones.EsperarTecla()

        elif opcion == "4":
            print("Saliendo del módulo de ventas.")
            funciones.EsperarTecla()

        else:
            print("Opción inválida. Intenta de nuevo.")
