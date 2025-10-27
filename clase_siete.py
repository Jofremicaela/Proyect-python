
## ejemplo metodo append()

""" ventas = [1,2,3]
ventas.append(100)

print(ventas)  """ 

# Salida: [1,2,3,100]

## ejercicio practico: crar una lista vacia de ventas,agregar a la lista venta.append(monto) , crear bucle while para recopilar datos y  usar bucle for para imprimir ventas <>
""" 
ventas = []
contador = 0
while contador < 4 :
    monto= int(input('Ingrese el valor del producto: '))
    contador+=1
    ventas.append(monto)
for monto in ventas:
    print('Valor ingresado:', monto) """
    

""" 
## ejemplo metodo remove()
productos = ["pan", "leche", "queso"]
productos.remove("pan")

print(productos)  
# Salida: ["leche", "queso"] """

##Ejercicio final de clase 7

""" En TalentoLab necesitamos llevar un registro ordenado de los nombres de los nuevos y nuevas clientes que se van incorporando.Tu tarea es escribir un programa en Python que haga lo siguiente:

Solicite los nombres de los y las clientes uno por uno, y valide que cada nombre no esté vacío. Si se deja el campo vacío, mostrar un mensaje de advertencia y pedir nuevamente el nombre.
Guarde cada nombre válido en una lista, asegurándote de agregarlo con el método .append(). 

Permití que se finalice la carga de nombres escribiendo la palabra "fin". 

Una vez finalizada la carga, ordená alfabéticamente los nombres en la lista y mostrá la lista ordenada utilizando un bucle for. """


lista_nombres=[]
while True:
    nombre = input("Ingrese su nombre: ")
    if nombre == "":
        print("Error!, vuelve a ingresar tu nombre.")
        continue 
    lista_nombres.append(nombre)

    for nombre in lista_nombres.sort():
        print(lista_nombres)
    

