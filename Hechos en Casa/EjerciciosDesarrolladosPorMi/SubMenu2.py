from .Ejercicios import *

def mostrar_submenu2():

    while True:
        print("======== SUBMENÚ DE EJERCICIOS ========")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Ejercicio 8")
        print("9. Ejercicio 9")
        print("10. Ejercicio 10")
        print("0. Regresar al Menú Principal")

        opcion = int(input("\nElija un ejercicio (1-10): "))

        match opcion:

            case 1:
                ejercicio1PN()
                input("\nPresiona Enter para regresar al submenú...")

            case 2:
                ejercicio2Edades()
                input("\nPresiona Enter para regresar al submenú...")

            case 3:
                ejercicio3ParesImpares()
                input("\nPresiona Enter para regresar al submenú...")

            case 4:
                ejercicio4Descuento()
                input("\nPresiona Enter para regresar al submenú...")

            case 5:
                ejercicio05SistemaAhorro()
                input("\nPresiona Enter para regresar al submenú...")

            case 6:
                ejercicio06BloqueoPin()
                input("\nPresiona Enter para regresar al submenú...")

            case 7:
                ejercicio07TipoMixto()
                input("\nPresiona Enter para regresar al submenú...")

            case 8:
                ejercicio08BusquedaBandera()
                input("\nPresiona Enter para regresar al submenú...")

            case 9:
                ejercicio09ConversionyMenu()
                input("\nPresiona Enter para regresar al submenú...")

            case 10:
                ejercicio10EstudiantesAprobados()
                input("\nPresiona Enter para regresar al submenú...")

            case 0:
                print("Regresando al menu principal...")
                input("\nPresiona Enter para regresar al submenú...")
                break

            case _:
                print("\nOpcion ingresada invalida...")
                input("\nPresiona Enter para regresar al submenú...")