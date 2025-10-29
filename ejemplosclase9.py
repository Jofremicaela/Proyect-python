

# Lista vacía para almacenar las frutas
frutas = []
# Función para agregar una fruta a la lista
def agregar_fruta():
    fruta = input("Ingresá el nombre de la fruta que querés agregar: ").capitalize()
    frutas.append(fruta)
    print(f"Fruta '{fruta}' agregada con éxito.\n")
# Función para consultar (mostrar) todas las frutas en la lista
def consultar_frutas():
    if frutas:
        print("Lista de frutas:")
    for i, fruta in enumerate(frutas, start=1):
        print(f"{i}. {fruta}")
    else:
        print("La lista de frutas está vacía.")
        print()
# Función para borrar una fruta de la lista

def borrar_fruta():
    if frutas:
        fruta = input("Ingresá el nombre de la fruta que querés borrar: ").capitalize()
        if fruta in frutas:
            frutas.remove(fruta)
            print(f"Fruta '{fruta}' eliminada con éxito.\n")
        else:
            print(f"La fruta '{fruta}' no está en la lista.\n")
    else:
        print("La lista de frutas está vacía. No hay nada para borrar.\n")

# Función para mostrar el menú y manejar las opciones del usuario
def mostrar_menu():
    while True:
        print("Menú de gestión de frutas:")
        print("1. Agregar una fruta")
        print("2. Consultar la lista de frutas")
        print("3. Borrar una fruta")
        print("4. Salir")
        opcion = input("Elegí una opción (1-4): ")
        if opcion == "1":
            agregar_fruta()
        elif opcion == "2":
            consultar_frutas()
        elif opcion == "3":
            borrar_fruta()
        elif opcion == "4":
            print("¡Gracias por usar el programa! ¡Chau!")
            break
        else:
            print("Opción no válida. Por favor, ingresá un número del 1 al 4.\n")
# Llamada inicial para ejecutar el menú
mostrar_menu()