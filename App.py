from colorama import Fore, init
from database import inicializar_db
from funciones import (
    agregar_producto,
    mostrar_productos,
    actualizar_producto,
    eliminar_producto,
    buscar_producto,
)

# Inicializacion de colorama
init(autoreset=True)


def menu():  # Menu principal
    while True:
        print(
            Fore.CYAN
            + "-------------------------\nMenu Principal\n-------------------------")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Salir")
        opcion = input(Fore.YELLOW + "Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            print(Fore.CYAN + "Saliendo del sistema...")
            break
        else:
            print(Fore.RED + "Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    inicializar_db()
    menu()
