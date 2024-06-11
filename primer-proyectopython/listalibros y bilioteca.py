

numeros = [1,2,3,4,5]
suma = sum (numeros)
print("la suma de los elementos de la lista es.",suma)
libros=[]
autores=[]

while True:
    
    print (" menu")
    print ("1.- añadir libro.")
    print ("2.-buscar libro.")
    print ("3.-eliminar libro.")
    print ("4.-salir.")

    opc = input("selecione una opcion:")
    
        ####### añadir
    if  opc == 1:
        nombre= input("ingrese el nombre del numeros")
        autor = input("ingrese el nombre el autor:")
        libros.append(nombre)
        autores.append(autor)
        print("libro añadido exitosamente.")
        ########## buscar
    elif opc == 2:
        nombre = input("ingrese el nombre del libro a buscar:")
        if nombre in libros :
            indice = libros.remove(nombre)
            libros.pop(indice)
            autores.pop(indice)
            print ("libro eliminado exitosamente:  ")
        else:
            print("el libro no se encuentra en la biblioteca")
            ########## eliminar
    elif opc == 3:
        nombre = input("ingrese el nombre del libro a eliminar:")
        if nombre in libros:
            indice = libros.remove(nombre)
            libros.pop(indice)
            autores.pop(indice)
            print("libro eliminado exitosamente")
        else:
            print("el libro no se enucnetra en la biblioteca")
    
      ########### salir del progrmas
    elif opc == 4:
        print("saliendo del programa")
        break

        


