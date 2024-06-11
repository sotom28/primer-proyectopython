usuarios =0
productos = {
    "Discos Duros": {"precio": 50000, "stock": 10},
    "Memorias Ram": {"precio": 35000, "stock": 3},
    "Placas Madre": {"precio": 40000, "stock": 10},
    "Fuentes de poder": {"precio": 40000, "stock": 0}
}
usuario_actual = None

while True:
    print("\nMenú Principal:")
    print("1.- Iniciar Sesión")
    print("2.- Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        if nombre in usuarios:
            usuario_actual = usuarios[nombre]
            print(f"Bienvenido {nombre}!")
        else:
            usuarios=nombre = ="rol": "comprador"}
            usuario_actual = usuarios[nombre]
            print(f"Bienvenido {nombre}! Nuevo usuario registrado exitosamente.")
            
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")

    while usuario_actual is not None:
        if usuario_actual["rol"] == "administrador":
            print("\nMenú Administrador:")
            print("1.- Dar de Alta usuario")
            print("2.- Abastecer Local")
            print("3.- Sacar Reporte")
            print("4.- Cerrar Sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre_nuevo = input("Ingrese nombre del nuevo usuario: ")
                usuarios[nombre_nuevo] = {"rol": "comprador"}
                print(f"Usuario {nombre_nuevo} registrado exitosamente.")
            elif opcion == "2":
                for producto, info in productos.items():
                    cantidad = int(input(f"Ingrese cantidad a agregar para {producto}: "))
                    info["stock"] += cantidad
                print("Stock actualizado.")
            elif opcion == "3":
                print("Reporte de inventario:")
                for producto, info in productos.items():
                    print(f"{producto}: {info['stock']} unidades")
            elif opcion == "4":
                print("Sesión cerrada.")
                usuario_actual = None
            else:
                print("Opción inválida. Intente de nuevo.")
        
        elif usuario_actual["rol"] == "comprador":
            print("\nMenú Comprador:")
            print("1.- Comprar Productos")
            print("2.- Pagar Cuenta")
            print("3.- Cerrar Sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("Productos disponibles:")
                for producto, info in productos.items():
                    print(f"{producto}: ${info['precio']}")

                producto_seleccionado = input("Seleccione un producto: ")
                cantidad_deseada = int(input("Ingrese la cantidad deseada: "))

                if producto_seleccionado in productos:
                    if productos[producto_seleccionado]["stock"] >= cantidad_deseada:
                        productos[producto_seleccionado]["stock"] -= cantidad_deseada
                        print(f"Compra realizada. Total a pagar: ${productos[producto_seleccionado]['precio'] * cantidad_deseada}")
                    else:
                        print("Lo sentimos, no hay suficiente stock disponible.")
                else:
                    print("Producto no encontrado.")
            elif opcion == "2":
                total = sum(info["precio"] * info["stock"] for info in productos.values())
                print(f"Total a pagar: ${total}")

                pago = float(input("Ingrese el monto a pagar: "))
                while pago < total:
                    pago = float(input("El monto ingresado es menor al total. Por favor, ingrese un monto válido: "))

                descuento = input("¿Tiene código de descuento? (Sí/No): ")
                if descuento.lower() == "sí":
                    codigo_descuento = input("Ingrese el código de descuento: ")
                    if codigo_descuento == "DESCUENTODELMES":
                        total *= 0.9
                        print(f"Descuento aplicado. Nuevo total a pagar: ${total}")
            elif opcion == "3":
                print("Sesión cerrada.")
                usuario_actual = None
            else:
                print("Opción inválida. Intente de nuevo.")