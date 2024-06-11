
condciones=0
opc=0
correo=0
total_comprar=0
restar_comprar=0

condciones= (input("debera ingresa si acepta condciones  o no aceptar condicones"))
if condciones.lower()== "si":
    print("continuando...")
    correo=input("por favor, ingrese su dirrecion de correo :")

    while opc != 3:
    try:   
        print ("menu : ")
        print("1.-agregar compar")
        print("2.-restar comprar")
        print("3.- salir")

        opc= input("seleciones una opcionm:")

        if opc== 1:
            print("opcion 1 slecionar agreagar comprar")
        elif opc== 2:
            print("opcion 2 slecionada restar comprar")
            total_comprar=total_comprar-restar_comprar

        elif opc == 3:
            print("saliendo del programas")
            total_comprar=0 ###
            enviar_cooreo =input("desear enviar una compia por el cooreo electronico? (si/no) :")
        
        
        if enviar_cooreo.lower == "si":
                print( f"enviar el pago a la dirrecion de cooreo elelctronico {correo}")
            break
        
        
    except:
       
else:
    print("opcion invalida  por favor  selecione una opcion del menu.")    
        ####### aqui iria el codigo para enviar el cooreo electronico
   


elif condciones.lower() == "no":
    print("no ha acepatado los terminos y condiciones. el prtogramas no puede continuar")
else:   
    print ("repuesta no valida.por favor,ingrese "SI" o "no"." )
 
        

            

s