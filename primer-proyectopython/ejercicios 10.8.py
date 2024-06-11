inventario = []

def añadir_producto():
    nombre = input("ingrese el nombre del productos")
    cantidad = int(input("ingrese la cantidad del producto"))
    precio = float(input("ingrese el precio del prdcuto:"))
    prducto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(prducto)

def eliminar_producto():
    nombre = input ("ingrese el nombre del producto a eliminar")
    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            print ("producto  eliminado exotosamente.")
            return
    print("producto no encontrado.")

def actualizar_cantidad():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            producto["cantidad"] = nueva_cantidad
            print("Cantidad actualizada exitosamente.")
            return
    print("Producto no encontrado.")

def mostrar_inventario():
    if not inventario:
        print("el inventario esta vacio.")
    else:
        print("inventario:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
            return 

def buscar_producto():
    nombre = input ("ingrese el nombre del producto a buscar:")
    for producto in inventario:
        if producto ["nombre"] == nombre:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
            return
    print("producto no encontrado.")

##### menu interativo
def menu():
    while True:

        print("menu de gestion de inventarios")
        print("1.- añadir producto")
        print("2.-eliminar producto")
        print("3.-actualizar producto")
        print("4.-mostrar invetanrio ")
        print("5.-mostar inventario ")
        print("6.-salir")

        opc = input ("seleccione una opcion :")

        if opc == "1":
            añadir_producto()
        elif opc == "2":
            eliminar_producto()
        elif opc == "3":
            actualizar_cantidad()
        elif opc == "4":
            mostrar_inventario()
        elif opc == "5":
            buscar_producto()
        elif opc == "6":
            print("salir del porgramas : ")
            break
        else:
            print("opcion invalida , intenterlo nuevamente:")
menu()


