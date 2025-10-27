"""  ejemplos de recorridos de listas usando for :
ejemplo 1
productos = ["manzanas", "piñas", "bananas", "uvas"]

for producto in productos:
    print("Producto disponible:", producto)

ejemplo 2

maquillaje = [ "labial", "rubor", "rimmel"]
for maquillajes in maquillaje:
        print ("El stock disponible es : ", maquillajes) """

""" 
##este codigo recorre la lista en busca del producto especifico, una vez encontrado el breack termina el ciclo

productos = ["P001", "P002", "P003", "P004", "P005"]
producto_a_buscar = "P003"
for producto in productos:
    if producto == producto_a_buscar:
        print("Producto encontrado:", producto)
        break
    print("Buscando...")
print("Fin de la búsqueda.") """


""" 

## ejemplo de range(fin)

for i in range(5):
    print(i)

    ##ejemplo de range(inicio, fin)

for i in range(3, 7):
    print(i)
    
for i in range(0, 10, 2):
    print(i)

    
## ejemplo de range(inicio, fin, paso)

for i in range(10, 0, -2):
    print(i) """

""" 
Imprime cada fruta con su número de posición, con len () obtenemos la cantidad de elementos del objeto frutas

frutas = ["manzana", "banana", "naranja"]
for i in range(len(frutas)):
    print(f"Fruta {i+1}: {frutas[i]}") """


""" for i in range(5):
    if i == 2:
        continue
    print(i) """

""" 
frutas = ["manzana", "banana", "naranja"]
for i, fruta in enumerate(frutas, start=1):
    print(f"Fruta {i}: {fruta}")
 """

""" ingresos = [40000, 55000, 60000, 45000, 70000, 50000]
count = 0

for ingreso in ingresos:
    if ingreso > 50000:
        count += 1

print(f"Cantidad de ingresos superiores a $50000: {count}") """

""" numeros = [10, 20, -30, 40, -50]

suma = 0

for numero in numeros:

    if numero < 0:

        continue

    suma += numero

print(suma) """

##Ejercicio final de clase seis

""" PARTE 1:

Crear una lista con los nombres de los y las clientes que vamos a procesar. Recorrer la lista y mostrar el nombre de cada cliente o clienta, junto con su posición en la lista (por ejemplo, Cliente 1, Cliente 2, etc.).

Recorrer la lista con un for y mostrar el nombre de cada cliente junto con su posición en la lista (por ejemplo: Cliente 1: Ana).

Si encuentras un nombre vacío, mostrar un mensaje de alerta indicando que ese dato no es válido.

Ejemplo de salida:

Cliente 1: Ana
Cliente 2: Juan
Cliente 3: [ALERTA] Nombre no válido
Cliente 4: Marta 

PARTE 2:

Además, como bonus, probá aplicar el método .capitalize() de Python, que sirve para poner en mayúscula la primera letra de una palabra y en minúscula el resto.

Ejemplo:

nombre = "mArIa"
print(nombre.capitalize())

Usalo para que los nombres válidos siempre aparezcan en el formato correcto, sin importar cómo estén escritos en la lista.je de alerta indicando que ese dato no es válido.
"""

lista_nombres= ['JUAN', 'NORMA','', 'JOSE', 'MARIANA']

for i, nombre in enumerate(lista_nombres, start=1) :
   
    if nombre == "" :
      print ("[ALERTA!] Nombre no valido")
    else:
     print(f"Nombre {i}: {nombre.capitalize()}")

     nombre= input
    


    
