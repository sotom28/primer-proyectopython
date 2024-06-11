import getpass

usuarios = {}

while True:
    print("1.- Registrar Usuario")
    print("2.- Iniciar Suma")
    print("3.- Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre_usuario = input("Ingrese nombre de usuario: ")
        contraseña = getpass.getpass("Ingrese contraseña: ")
        usuarios[nombre_usuario] = contraseña
        print("Usuario registrado exitosamente.")
    
    elif opcion == "2":
        nombre_usuario = input("Ingrese nombre de usuario: ")
        contraseña = getpass.getpass("Ingrese contraseña: ")
        
        if nombre_usuario in usuarios and usuarios[nombre_usuario] == contraseña:
            cantidad_numeros = int(input("Ingrese la cantidad de números que desea sumar: "))
            total = 0
            for i in range(cantidad_numeros):
                numero = float(input(f"Ingrese el número {i+1}: "))
                total += numero
            print("La suma total es:", total)
        else:
            print("Usuario o contraseña incorrectos. Vuelva a intentarlo.")
    
    elif opcion == "3":
        total_suma = sum([total for total in usuarios.values() if isinstance(total, float)])
        print("Total de números sumados:", total_suma)
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")