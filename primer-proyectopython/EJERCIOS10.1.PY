nombres =[]
apellidos=[]

def agregarnombres():
   
    nombres= input("ingrese el nombre ")
    apellidos=input("ingrese el apellidos ")
    nombres.append (nombres)
    apellidos.append(apellidos)
    print (f"aca se agregado el nomnbre y apellido {nombres + apellidos}")

def buscar_pornombre(nombrebusca):
    if nombrebusca in nombres:
        indice = nombres.index(nombrebusca)
        nombre=nombres [indice]
        apellido=apellidos [indice]
        print(f"nombre: {nombre},apellido:, {apellidos} ")
    else:
        print("nombre no encontrado.")

while True:
    print("menu") 
    print("1.-agregar nombre y apellido: ")
    print("2.-buscar por nombre :")
    print("3.-salir")
    opc = input("selecione una opcion ")
    
    if opc == "1" :
        agregarnombres()
    elif opc == "2":
        nombrebusca=input("ingrese el nombre el nombre que desea buscar")
        buscarnombres = (nombrebusca)
    elif opc == "3" :
        print("salir del porgramas")
        break
    else:
        print("opcion invalida, intenta nuevamente")








    