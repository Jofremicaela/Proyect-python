""" 
1- Ingreso de datos de productos: El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos). Estos datos deben almacenarse en una lista, donde cada producto sea representado/a como una sublista de tres elementos (nombre, categoría, y precio).
2- Visualización de productos registrados: El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos ingresados. La información debe presentarse de manera ordenada y legible, con cada producto numerado.
3- Búsqueda de productos: El sistema debe permitir buscar productos por su nombre. Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan. Si no hay coincidencias, debe informar que no se encontraron resultados.
4- Eliminación de productos: El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista.

requisitos: 
Usar listas para almacenar y gestionar los datos. 
Incorporar bucles while y for según corresponda. 
Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos.
Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias.
Presentar un menú que permita elegir entre las funcionalidades disponibles: agregar productos, visualizar productos, buscar productos y eliminar productos.
El programa debe continuar funcionando hasta que se elija una opción para salir.

"""



productos=[
                ["queso","almacen", 1000],
                ["jugo","almacen", 200],
                ["shampoo","higiene", 5000]
]
opcion= 0

while opcion != '5':
    print('\n Menu de opciones: ')

    print("\n 1. Agregar producto",
            "\n 2. Mostrar productos",
            "\n 3. Buscar producto",
            "\n 4. Eliminar producto",
            "\n 5. Salir \n")

    opcion = input(" Elige una opción: ")

    if opcion == '1':
        
        nombre = input (" Nombre del producto: ").strip()
        categoria = input ("Categoria del producto: ").strip()
        precio = int(input(" Precio del producto: "))

        if nombre != "" :
            productos.append([nombre, categoria, precio])
            print("Producto agregado exitosamente.")
        else :
                print ("Ingrese valores validos.")

    elif opcion == '2':

        for i in range(0,len(productos),1):

            print('\n Lista de productos: ')

            print(f"Nombre: ", productos[i][0])
            print(f"Categoria:" ,productos[i][1])
            print(f"Precio: ", productos[i][2])
    
    elif opcion == '3':


        producto_buscar = input('Producto a buscar: ').strip().lower()
        encontrado = False 

        for producto in productos:
            if producto[0] == producto_buscar:
                encontrado = producto
        
        if encontrado:
                print('Producto encontrado:', encontrado)
        else:
            print('Producto no encontrado.')


    elif opcion == '4':
        
        indice = int(input("Ingrese el número del producto a eliminar: "))

        if 0 <= indice <= len(productos):
            eliminado = productos.pop(indice -1)
            print(f"Producto eliminado: {eliminado}")
        else:
            print("Número inválido")

    else:
        print ('Gracias por utilizar nuestro programa!.')

