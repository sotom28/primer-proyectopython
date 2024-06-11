
contraseña=0
contraseña1=0
contraseña2=0  
contraseña3=0
usuario =0
usuario1=0
usuario2=0
usuario3=0
opc=0
opc_user=0
numero_celular=0
numero_celular_insigit=0
numero_celular_startswith=0

####registro de usuarios
print("registro de usuarios : ")
for i in range (3):
        print (" deberas registarte.")
        usuario = input(f"ingrese el nombre de usuario {i+usuario}:")
        contraseña = input (f"ingrese la contraseña para {usuario}:")
        usuario[usuario1]= contraseña1
        usuario[usuario2]= contraseña2
        usuario[usuario3]= contraseña3
        print("\nBienvenido al sistema de inico de sesion")
###### ciclo pricipal
       
        while True:
        
            print ("1.- inciar sesion")
            print ("2.- salir")

            if opc <0 and opc > 2:
                print("opcion invalida")
                break
        if opc ==1 :
            ####### inicia sesion:") 
            usuario = input("ingresa su nombre de usuario: ")
            contraseña = input("ingrese su contraseña")
            if usuario in  usuario1 and usuario1 [usuario]== contraseña:
                usuario in  usuario2 and usuario2 [usuario]== contraseña
                usuario in  usuario3 and usuario3 [usuario]== contraseña      
                print ("sesion iniciada como", usuario)
                ####### menu de usuario
                while True:
                    
                    print ("menu de incio ") 
                    print ("1.-realizar llamada")
                    print ("2.-enviar correo electroncio")
                    print ("3.-cerrar sesion")

                    opc_user = input("selecione una opcion:")

                    if opc_user < 0 and opc_user >3:
                            print ("la opcion es invalida intertalo nuevamente")
                            break
                    else:
                        
                        if opc_user == 1:
                            #### realiza llamada
                            numero_celular = input("ingrese el numero de celular ( debe comenzar  con 9 digitos)")
                            if len(numero_celular) == 9 and numero_celular_insigit() and numero_celular_startswith("9"):
                                print("llamada realizada al numero:"), numero_celular
                            else:
                                print("numero de celular invalido , inteterlo nuevamente.")

                        elif opc_user == 2:
                            ######## ingresa el correo electronico y mensaje
                            correo = input("ingrese su correo electronico: ")
                            if "@" in correo:
                                mensaje = input ("ingrese su mensaje que va a enviar: ")
                                print ("correo electronico enaviado a:"), correo
                                print("mensaje enviando "), mensaje
                            else:
                                print(" correo electronico invalido. intentelo de nuevo.")

                        elif opc_user ==3:
                            ### cerrar sesion
                            print("cerrando sesion")
                            break
                        else:
                            print ("opcion invalidad, por favor , selecione una opcion validad.")
                    
        elif opc == 2:
                ###### salir de programa 
                print("saliendo del programa")
                break
        else:
            print(" opcion invalida.por favor, selecione una opcin validad")               


                            