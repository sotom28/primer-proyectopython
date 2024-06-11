
user1= None
user2 = None
user3 = None
password= None
password=  None
password3 = None
user=0
opc=0
opc_user=0
numero_celular=0
numero_indigit=0
numero_celular_startwith=0

while True:
    
    print ("\nBienvenido al sistema de incicio de sesion ")
    print("1.-iniciar sesion")
    print("2.-registrar usuario")
    print("3.-salir")

    opc = input("seleciona una opcion")

    if opc == 1 :   
        if not any([user1,user2,user3]):
            print("no hay usuarios registardos. por favor , registro un usuario ")
            break
        while True:
            user = input("ingrese su nombre de usuario : ")
            passwword = input("ingrese su contraseña :")1
     
            if user == user1 and passwword == passwword1:
                print ("sesion iniciada como user1")
                break
            elif user == user2 and passwword == passwword2:
                print("sesion inciada como user 2 ")
                break
            elif user == user3 and passwword == password3:
                print ("session iniciada como user3")
            else:
                print("sesion invalida, intertelo nuevamente")
        
            print("usurio o contraseña  incorrectos . inntente de nuevo.")
    elif  opc ==2:
        if any ([user1, user2 , user3]):
            print ("ya existen usuarios registardos .No se puede registar mas usuarios")
            continue

        user1 = "user1"
        passwword1= "password1"
        user2 = "password2"
        passwword2 = "password2"
        user3 = "user"
        password3 = "password3"
        print(" usuarios registrados correctamente.")
    
    elif opc == 3:
        print(" saliendo del programa  ")
    else:
        print("opcion invalida. por favor, seleciona opcion valida.")
        break
        ###### MENU DE USUARIO
    while True:
            print ("menu de usuario")
            print("1.- relizar llamada")
            print("2.- enviar correo electronico")
            print("3.- cerrar sesion")

            if opc_user <0 and opc_user >3:
                    print ("opciones es invalida")


            if opc_user == "1":
                    numero_celular = int(input("ingrese el numero de celular ( debe comenzar con 9 digitos)"))
                    if len(numero_celular) == 9 and numero_indigit and numero_celular() and numero_celular_startwith("9"):
                        print("llamda realizada al numero : ", numero_celular)
                    else:
                        print(" Numero de celular invalida.intente de nuevo.")

            elif opc_user == "2":
                    while True:
                        correo = input("ingrese su correo electronico: ")
                        if "@" in correo:
                            print("el correo funciona correctamene")
                        else:
                            print ("correo electronico invalido, intente de nuevo")
                            continue
                        mensaje= input("ingrese el mensaje que va enviar")
                        print("correo electonico enviado a :", correo )
                        print("mensaje:",mensaje)
            elif opc_user == "3":
                #cerrar sesion
                    print("cerrar sesion :::")  
                
            else:   
                print("opcion invalida. Por favor , selecione  una opcion valida.") 
                break
