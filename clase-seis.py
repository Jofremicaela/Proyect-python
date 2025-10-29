
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
    


    
