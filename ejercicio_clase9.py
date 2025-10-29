
""" crear un programa en Python con las siguientes
características:
● Agregar productos: Permite a la usuaria o usuario
agregar productos a una lista. Cada producto debe
tener un nombre y un precio.
● Consultar productos: Muestra todos los productos en la lista junto con sus
precios.
● Eliminar productos: Elimina un producto de la lista a partir de su nombre.
● Menú interactivo: El programa debe ofrecer un menú para que el usuario o
usuaria pueda elegir qué acción realizar. Debe incluirse una opción para
salir del programa. """

productos={}


def agregar_producto ():
            
            producto= input("Ingrese el nombre del producto: ")
            precio=int(input("Ingrese el precio del producto: "))
            productos.update({producto: precio})
            print('cargado exitosamente.')
            print (productos)

def consultar_producto() : 
        
        print(f"\n Lista de productos: \n",f"\n Producto: {nombre}",f"\n Precio: ${productos[nombre]}") if (nombre := input("Ingrese el nombre del producto: ").strip().lower()) in productos else print("\n Producto no encontrado")


def eliminar_producto() :
    if productos:
        producto = input("Ingresá el nombre : ").strip().lower()
        if producto in productos:
            del productos[producto]
            print(f"\n Producto '{producto}' eliminado con éxito.\n")
        else:
            print(f"\n El producto '{producto}' no está en la lista.\n")
    else:
        print("\n La lista de productos está vacía. No hay nada para borrar.\n")




def menu_opciones ():
    opcion= 0

    while opcion != 4 :
        print ("\n Menu de opciones")
        
        print (" 1. Agregar producto")
        print (" 2. Consultar producto")
        print (" 3. Eliminar producto")
        print (" 4. Salir")

        opcion= input("\n Elige una opcion: ")
        if opcion == "1":
                    agregar_producto ()
        elif opcion == "2":
                    consultar_producto()
        elif opcion == "3":
                    eliminar_producto() 
        elif opcion == "4":
                    print("¡Gracias por usar el programa!")
                    break
        else:
                print("Opción no válida. Por favor, ingresá un número del 1 al 4.\n")
    

menu_opciones()