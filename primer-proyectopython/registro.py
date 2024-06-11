import getpass
opc = 0
usuarios ={}

while True:
        print ("1.- registar usuario")
        print ("2.- inciar suma")
        print ("3.- salir")

        opc = input(" seleciones una opcion:")
    ##M
        
        if opc == 1 :
            nombre_usuario = input("ingrese nombre de usuario:")
            contraseña = getpass("ingrese contraseña")
            usuarios [nombre_usuario] = contraseña
            print("usario registrado exitosamente.")
       
        elif opc ==2 :
            nombre = input("ingrese nombre de usuario:" )
            contraseña=getpass.getpass("ingrese la contraseña: ")
        
        if nombre_usuario in usuarios and usuarios [nombre_usuario] == contraseña:
                cantidad_numeros = int(input("ingresde la cantidad de numeros que desea sumar"))
                total = 0
                for i in range (cantidad_numeros):
                    numero = float(input( f" ingrese numero {i +1}:" ))
                    total += numero 
                    print ("las suma total es :", total )
        else:
            print ("usuario o contraseña incorrectos. vulva a intertarlo.")

        if opc == 3 :
            total_suma = sum([total for total in usuarios.values () if isinstance ( total, float)])
            print ("total de numeros sumados:", total_suma)  
            break               
        else:
            print ("opcion no valida. por favor, seleccione una opcion validad." )        