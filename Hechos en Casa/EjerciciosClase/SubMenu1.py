from .PrimerosEjercicios import ejercicios01
from .SegundosEjercicios import ejercicio02
from .TercerosEjercicios import ejercicios03
from .CuartoEjercicio import ejercicio04
from .QuintoEjercicio import ejercicio05

def mostrar_submenu():
    while True:
        print("======== SUBMENÚ DE EJERCICIOS  ========")
        print("1. Ejercicios 1 (Tipos de Datos, Variables y Condicionales)")
        print("2. Ejercicio 2 (Condicionales 2 - Notas)")
        print("3. Ejercicios 3 (Ciclo For)")
        print("4. Ejercicios 4 (Ciclo For 2 - Notas)")
        print("5. Ejercicio 5 (Ciclo For 3 - Factorial)")
        print("0. Regresar al Menú Principal")

        opcion = input("\nElija un ejercicio (1-5): ")

        match opcion:
            case '1':
                print("Ejecutando Ejercicios 1...")
                ejercicios01()
                input("\nPresiona Enter para regresar al submenú...")

            case '2':
                print("Ejecutando Ejercicio 2...")
                ejercicio02()
                input("\nPresiona Enter para regresar al submenú...")
            case '3':
                print("Ejecutando Ejercicios 3...")
                ejercicios03()
                input("\nPresiona Enter para regresar al submenú...")
            case '4':
                print("Ejecutando Ejercicio 4...")
                ejercicio04()
                input("\nPresiona Enter para regresar al submenú...")
            case '5':
                print("Ejecutando Ejercicio 5...")
                ejercicio05()
                input("\nPresiona Enter para regresar al submenú...")
            case '0':
                print("Regresando al menu principal...")
                break
            case _:
                print("\nOpción no valida.")
                input("Presiona Enter para intentar de nuevo...")