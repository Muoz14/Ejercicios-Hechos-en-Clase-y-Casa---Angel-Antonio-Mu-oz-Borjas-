from EjerciciosClase.SubMenu1 import mostrar_submenu
from EjerciciosDesarrolladosPorMi.SubMenu2 import mostrar_submenu2

while True:

    print(f"========= MENU DE EJERCICIOS =========\n")
    print(f"1. Ejercicios Hechos en Clase")
    print(f"2. Ejercicios Desarrollados por mi")
    print(f"0. Salir del programa")

    op = input("\nIngrese una opción: ")

    match op:

        case '1':

            print(f"========= EJERCICIOS HECHOS EN CLASE =========\n")
            mostrar_submenu()

        case '2':
            print(f"========= EJERCICIOS DESARROLLADOS POR MI =========\n")
            mostrar_submenu2()

        case '0':
            print("\nPrograma finalizado....")
            break

        case _:

            print("\nOpcion ingresada es incorrecta o no existe....")
            input("Precione 'Enter' para continuar")