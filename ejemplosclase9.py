

##el siguiente codigo solo saluda con el nombre q le ingreses, sino por defecto saluda como
nombre=input("Ingrese su nombre: ")
def saludar(nombre="Invitado"):
    print(f"¡Hola, {nombre}!")
if nombre!="":
    saludar(nombre)
else : 
    saludar ()

