condiciones = input("¿Acepta los términos y condiciones? (si/no): ")

if condiciones.lower() == "si":
    print("Continuando...")
    correo = input("Por favor, ingrese su dirección de correo electrónico: ")

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Restar compra")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Opción 1 seleccionada: Agregar compra")
            # Aquí iría el código para agregar una compra
        elif opcion == "2":
            print("Opción 2 seleccionada: Restar compra")
            # Aquí iría el código para restar una compra
        elif opcion == "3":
            print("Saliendo del programa...")
            total_compra = 0  # Aquí iría el cálculo del total de la compra
            enviar_correo = input("¿Desea enviar por correo electrónico el pago? (si/no): ")
            if enviar_correo.lower() == "si":
                print(f"Enviando pago a la dirección de correo electrónico: {correo}")
                # Aquí iría el código para enviar el correo electrónico
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

elif condiciones.lower() == "no":
    print("No ha aceptado los términos y condiciones. El programa no puede continuar.")
else:
    print("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")