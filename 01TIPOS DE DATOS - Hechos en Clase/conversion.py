from Clases.FormulasConversion import FormulasConversion

import os
os.system('cls' if os.name == 'nt' else 'clear')

def ingresarGrados(metodo_conversion, nombreC):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(nombreC)

    g = float(input("Ingrese los grados: "))
    
    conversion = FormulasConversion(g)

    metodo_conversion(conversion)
    
    input("\nEnter para continuar...")

opcion = 1

while(opcion != 0):

    print("======= MENU DE CONVERSIONES =======\n")
    print("\t1. Grados Celsius a Fahrenheit")
    print("\t2. Grados Celsius a Kelvin")
    print("\t3. Grados Celsius a Rankine")
    print("\t4. Grados Fahrenheit a Celsius")
    print("\t5. Grados Fahrenheit a Kelvin")
    print("\t6. Grados Fahrenheit a Rankine")
    print("\t7. Grados Kelvin a Celsius")
    print("\t8. Grados Kelvin a Fahrenheit")
    print("\t0. Salir")

    opcion = int(input("\nIngrese una opcion: "))

    match opcion:
        
        case 1:
            ingresarGrados(FormulasConversion.cGradosFahrenheit, "CONVERTIR CELCIUS A FAHRENHEIT\n")

        case 2:
            ingresarGrados(FormulasConversion.cGradosKelvin, "CONVERTIR CELCIUS A KELVIN\n")

        case 0:
            print("Programa Finalizado.....")
            break
        
        case _:
            print("Opcion ingresada es incorrecta o no existe.....")
            input("\nEnter para continuar...")
