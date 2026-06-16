def ejercicios01():
    # Tipos de datos

    print("\nTipos de Datos")

    nombre = input("Cual es tu nombre? ")

    print(f"Hola {nombre}")

    edad = int(input("Ingresa tu edad: "))

    print(f"{nombre} tienes {edad} años")

    # Variables

    print("\nVariables")

    print("Ecuacion lineal: ax + b = 0")
    a = int(input("a: "))
    b = int(input("b: "))
    x = -b / a
    print(f"x {str(x)}")
    print(f"x es de tipo: {str(type(x))} ")

    # Variables de tipo booleanas 1

    print("\nVariables de tipo booleanas 1")

    z = True
    print(f"z: {str(z)}")
    print(f"x es de tipo: {str(type(x))} ")

    # Condicionales

    print("\nCondicionales (a no puede ser 0)")

    print("Ecuacion lineal: ax + b = 0")
    a = int(input("a: "))
    if a == 0:
        print("No es una ecuacion lineal")
    else:
        b = int(input("b: "))
        x = -b / a
        print(f"x {str(x)}")
        print(f"x es de tipo: {str(type(x))} ")

    # #Variables de tipo booleanas 2

    print("\nVariables de tipo booleanas 2")

    z = None  # Es basicamento nulo porque no tiene un espacio en memoria asignado.
    if z:
        print(f"z: Es Verdadero {str(z)}")
    else:
        print(f"z: Es Falso {str(z)}")

    print(f"x es de tipo: {str(type(z))} ")