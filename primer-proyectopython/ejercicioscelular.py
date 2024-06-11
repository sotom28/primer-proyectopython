opc= 0

user=[None]
user=[None]
user=[None]
password=[None, None, None]


while  opc != 3:
    print ("1).-inciar sesion:") 
    print ("2).-registrar usuario")
    print ("3).-salir")
try:
    opc=int(input("seleciona una opcion"))

    if opc < 0  and opc > 3:
            print("la opcion que escogiste es invalido")
        
    
    if opc == 1:
            ####### verificar si hay usuaruis registrados
            print("debera inicia sesion")
        
    if all (user is None for user in user ):
            print(" no hay usuarios. registrados,por favor resgistrar el usuario primero")
    else:
            print("error de registrado intentelo nuevamente")
            
except:
            print("value error")
        ############## solicitar usuario y contraseñas:
            usuario_ingresado=input("Ingrese su usuario:")
            password_ingresada=input("ingrese contraseña:" )

        ####### valida usuario de inicar sesion
            usuario_valido = False
            for i, user in enumerate (user):
              if user == usuario_ingresado and password[i] == password_ingresada:
                    print("incio de sesion exitoso. ")
                    usuario_valido= True
                    ######## MENU DEL USUARIO 
                    while True:
                        print(" menu de usuario")
                        print("1).- realizaar llamada")
                        print("2.-enviar correo electronico")
                        print("3.-cerrar session")
                        opc_user =input("seleciones una opcion")
                        if opc_user== 1:
                            numero_celular= input("ingrese el numero de celular (debe tener 9 digitos)")
                            if numero_celular (9) and len( numero_celular)==9:
                                print("llamada realizada al numero", numero_celular)
                            else:  
                                print("numero de celular invalido.")
                        
                        elif opc_user == 2:
                            correo=input("ingresa su correo elelectronico: ")
                            while "@" not in correo:
                                print("correo electronico invalido.debe contener al menos @")
                                correo = input("ingrese su cooreo electronico: ") 
                                mensaje = input("ingrese el mensaje a enviar")
                                print("correo electronico enviado a ", correo , "con el mensaje:", mensaje )
                        elif opc_user==3:
                            print(" session cerrada") 
                            break
                        else:
                            print("opcion invalida,vuelva a colocar una opcion")
                            break
                    if not usuario_valido:   
                        print("el usuario y la contraseña estan incorrectos,por favor intenterlo de nuevo")
                    elif opc ==2:
                        print ("registro de usuario")
                        for i, user in enumerate(user):
                            if user is None:
                               user[i] = input("INGRESE EL el nombre usuario:")
                               password[i] = input("ingrese una contraseña") 
                               print("usuario registrado con exito:")
                               break
                            elif i == len (user)- 1:
                                print("ya se han registrado 3 usuarios.")
                    elif opc==3:
                        print("saliste del programas:::")
                        break
                    else:
                        print("opcion invalidad.por favor ingreese nuevamente la opciones.")

                             
      






    
