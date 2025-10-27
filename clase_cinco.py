'''
numero = 0
print("Ingresa numeros positivos para sumarlos. Ingresa 0 para terminar.")
suma = 0
while True:
   # Solicitamos al usuario un número
   numero = int(input("Ingresa un numero:"))
   # Verificamos si el número es negativo
   if numero < 0:
       print("El numero es negativo, se ignora. Intenta de nuevo.")
       continue  
   if numero == 0:
       break
   suma += numero
print(f"La suma de los números positivos es: {suma}")
'''


'''
## uso de listas con while

numeros = [10, 20, 30, 40, 50]
indice = 0

while indice < len(numeros):
   print(f"El valor en el índice {indice} es: {numeros[indice]}")
   indice += 1

print("Fin del bucle.")

'''

""" ejercicico final de clase cinco """

    
meses = 0
while meses < 6 :
    ingreso = input('Ingresa el monto abonado de este mes: ')
    meses =+1


    if ingreso < 0:
        print ('El valor no es valido, debe ingresar numeros positivos. ')
    continue

