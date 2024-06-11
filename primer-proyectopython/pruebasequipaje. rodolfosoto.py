opc=0
opcsub=0
equipaje=0
cantidad=0
total_pagar=0
edad=0
opcsub2=0
peso=0
pago=0
#### ´programas equipaje
while True:
    
        print("menu principal")
        print("1.-ingresar ckeck-in :")
        print("2.-pagar check in")
        print("3.-salir")
        if opc<0 and opc>3:
            print("opcion es invalida , interterlo nuevamente")
    
        opc=input("ingresa una opcion valida")
        ########### ingresar submenu agregar y quitar equipaje
    

            
        if opc =="1":

            while opcsub != 3:
            try:       
                print ("ingresa al sub menu")
                print("1.- agrega equipaje") 
                print("2.-restar equipaje") 
                print("3")

                opcsub = input("ingresa la opcion del submenu")
            
                if opcsub == 1:
                    usuario = (input("ingresar nuevo usuario "))
                    equipaje=input ("cantidad que de desear agregar {equipaje}")
                    equipaje = agregarequipaje + agregarequipaje
                
                    agregarequipaje = equipaje + cantidad
                    for equipaje in cantidad:
                        print("el producto equipado, se guardardo existosamente.")
                    else:
                        print(" equipaje ingresado , esta invalido, intenterlo nuevamente. :")
                        break
            except:
                    
    
        ############ quitar equipaje
        try:        
            if opcsub == 2:
                    usuario = input(" ingresar el nuevo usuario ")
                    quitarequipaje = equipaje-cantidad
                    for equipaje in cantidad:
                        print("el producto equipado . se quitado existosamente")
                    else:
                        print("equipaje quitado, esta invalido, interterlo nuevamente. : ")
                        break

            #################### a salido sub menu 1  
            elif opcsub==3:
                print("salir")
                break

        except:    
                (ValueError)
                if opc ==2:     
        
                    
                    pago=input (" deber ingresa monto a pagar{total_pagar}")
                if pago < total_pagar :
                    print ("el pago es menor a la total  total, debera tener mas dinero")
                elif pago == total_pagar:
                    print ("se pago total se a pagado exitosamente no tiene deuda")
                total_pagar=0
    
        
                descuento=input("tiene descuento asosiado {descuento} (si / no)"), 
                if opc == "si" :
                    print("debera ingresa la edad para obtener el descuento{edad}")
                else:

                    if edad  >0 and edad > 15:
                        print(f" usuario que tenga o 15 años  no tiene descuento {descuento}")
                        total_pagar= pago *0
                    elif edad >17 and edad>59:
                        print("el usuario que tenga 17 a 59 tiene un descuento de 15% {descuento}")
                        total_pagar = pago * (descuento * 0.15)
                    elif edad <60 and edad>100  :
                        print("el usuario que tena 60 años a mas tendra un descuento de 20%{descuento}")
                        total_pagar= pago * (descuento*0.20)
                        break
                        
                    ############## ingresa submenu 2 menu de la opcion agregar 
                    try:   
                        if opcsub2 ==1:
                            usuario_actual= (input("debera ingresa un nuevo usuario "))
                            usuario = usuario_actual
                            usuario_actual= equipaje 
                            peso  == equipaje 
                            agregarequipaje= equipaje + cantidad
                            peso = int(input ("cuanto kilo pesa tu equipaje"))
                            if peso < 10 and peso <19:
                                    print("el valor de 10 kilogramos es ${10000} ")
                            
                   
                            elif peso== 20 and peso <29:
                                print("el valor de 20 kilogramos es ${200000}")
                            
                            elif peso == 30 and peso > 40:
                                print("el valor de 30 kilogramos es ${30000}")
                            else:
                                print (" no se acepta de mayor de 40 kilo el equipaje")
                                break
                            ######restar equipaje
                    except:

                        try:
                            if opcsub2== 2:
                                usuario_actual= (input ("debera usar el nuevo usuario"))
                                usuario_actual = equipaje
                                peso = equipaje - cantidad
                                quitarequipaje = equipaje - cantidad ####### se quita equipaje eliminado
                                peso = int(input ("cuanto restar kilo pesa tu equipaje"))
                                if peso < 10 and peso <19:
                                    print("el valor de 10 kilogramos es ${10000-cantidad}  ")
                            
                   
                                elif peso== 20 and peso <29:
                                    print("el valor de 20 kilogramos es ${200000-}")
                            
                                elif peso == 30 and peso > 40:
                                    print("el valor de 30 kilogramos es ${30000}")
                                else:
                                    print (" no se acepta de mayor de 40 kilo el equipaje")
                                    break
                 
                        except:
                                    ######## salir sub menu 
                            if opcsub2 == 3:
                                print("salir de submenu y volver al menur principal")
                                break
                    
                        if opcsub2 == opc:
                            break
        if opc == 3:###### salir del programa
            print ("salir de programa")
            break
                    

            

                                   


                             
                    



                



            
                 


                          
        
        
                
             
        