


##- Registro de productos con precios

""" Tenés que construir un pequeño sistema para registrar productos que una persona va comprando.

Tu programa debe:

Usar un diccionario vacío al comenzar.
Pedir al usuario que cargue 3 productos con su precio.
Validar que el precio ingresado sea un número mayor a 0.
Guardar el producto como clave y el precio como valor.
Mostrar el contenido completo del diccionario.
Mostrar el total gastado, sumando todos los precios.
mostrar los productos en orden alfabético . <>"""

productos= { 
"leche": 200,
"peine": 100
}

for i in range(3):
        nombre = input("Ingrese el nombre del producto: ").strip().lower()
        precio = int(input("Ingrese el precio del producto: "))

        if nombre != "" and precio > 0:
                productos.update({nombre: precio})

                print('cargado exitosamente. ')

                print(productos)

        elif precio < 0:
                print('Valor no válido, debe ser mayor a cero.')
        else :
                print('Error. ')

print("\nLista de productos:")
for nombre, precio in sorted(productos.items()):
        print(f"Nombre: {nombre} | Precio: ${precio}")

total = sum(productos.values())
print(f"\nEl total de todos los precios es: ${total}")

