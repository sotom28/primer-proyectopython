# Inicialización de variables de usuarios y contraseñas
user1 = None
user2 = None
user3 = None
password1 = None
password2 = None
password3 = None

# Registro de usuarios
print("Registro de usuarios:")
user1 = input("Ingrese el nombre de usuario 1: ")
password1 = input("Ingrese la contraseña para {}:".format(user1))
user2 = input("Ingrese el nombre de usuario 2: ")
password2 = input("Ingrese la contraseña para {}:".format(user2))
user3 = input("Ingrese el nombre de usuario 3: ")
password3 = input("Ingrese la contraseña para {}:".format(user3))

print("\nBienvenido al sistema de inicio de sesión")
# Ciclo principal
while True:
    print("\n1.- Iniciar sesión")
    print("2.- Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Iniciar sesión
        print("\nInicio de sesión:")
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        if (usuario, contraseña) == (user1, password1) or \
           (usuario, contraseña) == (user2, password2) or \
           (usuario, contraseña) == (user3, password3):
            print("Sesión iniciada como", usuario)
            # Menú de usuario
            while True:
                print("\nMenú de usuario")
                print("1.- Realizar llamada")
                print("2.- Enviar correo electrónico")
                print("3.- Cerrar sesión")

                opcion_usuario = input("Seleccione una opción: ")

                if opcion_usuario == "1":
                    # Realizar llamada
                    numero_celular = input("Ingrese el número de celular (debe comenzar con 9 y tener 9 dígitos): ")
                    if len(numero_celular) == 9 and numero_celular.isdigit() and numero_celular.startswith("9"):
                        print("Llamada realizada al número:", numero_celular)
                    else:
                        print("Número de celular inválido. Inténtelo de nuevo.")
                elif opcion_usuario == "2":
                    # Enviar correo electrónico
                    correo = input("Ingrese su correo electrónico: ")
                    if "@" in correo:
                        mensaje = input("Ingrese el mensaje que va a enviar: ")
                        print("Correo electrónico enviado a:", correo)
                        print("Mensaje:", mensaje)
                    else:
                        print("Correo electrónico inválido. Inténtelo de nuevo.")
                elif opcion_usuario == "3":
                    # Cerrar sesión
                    print("Cerrando sesión.")
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        else:
            print("Usuario o contraseña incorrectos. Inténtelo de nuevo.")
    elif opcion == "2":
        # Salir del programa
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")