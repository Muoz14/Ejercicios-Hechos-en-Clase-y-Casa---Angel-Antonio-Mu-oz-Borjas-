def ejercicio1PN():
    # 1. Cálculo de Nómina y Horas Extras
    # Pide al usuario que ingrese las horas trabajadas en la semana y su pago por hora.
    # Si las horas superan las 40, las horas extra se deben pagar al 1.5 de la tarifa normal.
    # Muestra el salario total a pagar.

    print("Ejercicio 1 - Cálculo de Nómina y Horas Extras")

    ht = int(input("Ingrese las horas trabajadas en la semana: "))

    ph = float(input("Ingrese su pago por hora: "))

    if ht > 40:
        he = ht - 40
        phe = (he * (ph * 1.5))
        tp = ((ht - he) * ph) + phe
        print(f"Su pago final con horas extra es = {tp}")
    else:
        print(f"Su pago sin horas extra es de {ht * ph}")


def ejercicio2Edades():
    # 2. Categoría de Edad
    # Pide al usuario su edad. Si es mayor o igual a 18, imprime "Adulto".
    # Si está entre 13 y 17 (inclusive), imprime "Adolescente". Si es menor a 13, imprime "Niño".
    # Si el usuario ingresa un número negativo, imprime "Edad inválida".

    print("Ejercicio 2 - Categoría de Edad")

    edad = int(input("Ingrese su edad: "))

    if edad >= 18:
        print("\nUsted es un adulto")

    elif edad >= 13:
        print("\nUsted es un adolescente")

    elif edad >= 0:
        print("\nUsted es un niño")

    else:
        print("\nEdad invalida...")


def ejercicio3ParesImpares():
    # 3. Crea una lista de números fijos. Recorre la lista con un ciclo for.
    # Evalúa cada número e imprime si es "Par" o "Impar".

    numeros = [12, 7, 34, 23, 8, 15]

    print("Ejercicio 3 - Pares e Impares")

    for numeros in numeros:

        if numeros % 2 == 0:
            print(f"Es un numero par {numeros}")
        else:
            print(f"Es un numero impar {numeros}")


def ejercicio4Descuento():
    # 4. Crea una lista con precios. Utiliza un ciclo for.
    # Si el precio es mayor a 100, aplícale un 15% de descuento. Imprime el precio final de cada artículo
    # indicando si tuvo descuento o no.

    precios = [45.0, 120.0, 30.0, 250.0, 90.0]

    print("Ejercicio 4 - Aplicador de Descuento")

    for precio in precios:

        if precio > 100:
            descuento = precio - (precio * 0.15)
            print(f"El articulo de {precio} tuvo un descuento de 15% y el precio final es de {descuento}")

        else:
            print(f"El articulo de {precio} no tuvo desuento")

def ejercicio05SistemaAhorro():
    # 5. Tienes una meta de ahorro de $1000 y un saldo inicial de $0.
    # Crea un ciclo while que pregunte al usuario "¿Cuánto deseas depositar?". Suma ese valor al saldo e imprime el acumulado.
    # El ciclo debe detenerse únicamente cuando el saldo sea mayor o igual a la meta.

    print("Ejercicio 5 - Sistema de Ahorro")

    cantidad = 0.0
    deposito = 0.0

    while True:
        cantidad = float(input("Cuanto deseas depositar? "))
        deposito += cantidad
        print(f"Llevas acumulado: ${deposito}")
        if deposito >= 1000:
            break

    print(f"Tu saldo final acumulado es: ${deposito}")

def ejercicio06BloqueoPin():
    # 6. Define una variable con un PIN correcto. Crea un ciclo while que le dé al
    # usuario un máximo de 3 intentos para ingresar el PIN. Si acierta, imprime "Acceso concedido" y sal del ciclo.
    # Si falla los 3 intentos, imprime "Cuenta bloqueada".

    intentos = 0

    print("Ejercicio 6 - Bloqueo por PIN")

    while intentos < 3:

        contra = input("Ingrese la contraseña de acceso: ")

        if contra != "Hola123":
            print("Contraseña incorrecta...")
            intentos += 1
        else:
            print("Acceso concedido, bienvenido")
            break
    else:
        print(" Cuenta bloqueada....")

def ejercicio07TipoMixto():
    # 7. Crea una sola lista que contenga los datos de un empleado en este orden: nombre (string), número de empleado (int),
    # salario (float) y si está activo (booleano). Recorre la lista con un ciclo for e imprime cada valor seguido de su tipo de
    # dato usando la función type()

    empleado = ["Angel", 100, 2500.50, True]

    print("Ejercicio 7 - Registro de Empleado (Tipos de datos mixtos)")

    for dato in empleado:
        print(f"El dato {dato} del empleado es de tipo: {type(dato)}")

def ejercicio08BusquedaBandera():
    # 8. Crea una lista de productos en bodega: ["Monitor", "Teclado", "Raton", "Cable"]. Pide al usuario que ingrese el nombre de un artículo a buscar.
    # Usa una variable booleana como "bandera" (ej. encontrado = False). Recorre la lista; si el artículo está, cambia la bandera a True y rompe el ciclo con break.
    # Al final, revisa la bandera para imprimir "Artículo disponible" o "Artículo no encontrado".

    bodegaP = ["Monitor", "Teclado", "Mouse", "Cable"]
    pEcontrado = ""
    encontrado = False

    print("Busqueda de Inventario (Uso de Bandera)")

    busqueda = input("Ingrese el producto buscado: ")

    for producto in bodegaP:

        if busqueda == producto:
            encontrado = True
            pEcontrado = producto
            break

    if encontrado:
        print(f"El producto {pEcontrado} se encontro")
    else:
        print("El producto no se encontro")

def ejercicio09ConversionyMenu():
    # 9. Crea un menú dentro de un ciclo while True con 3 opciones: Convertir Celsius a Fahrenheit, Convertir Fahrenheit a Celsius
    # Salir.

    while True:
        print("========= Ejercicio 9 - MENU DE CONVERSION =========\n")
        print("1. Convertir Celcius a Fahrenheit")
        print("2. Convertir Fahrenheit a Celcius")
        print("0. Salir\n")

        opcion = int(input("Ingrese una opcion: "))

        match opcion:
            case 1:
                print("Convertir Celcius a Fahrenheit\n")
                celcius = float(input("Ingrese los grados Celcius: "))
                conversion = (celcius * 9 / 5) + 32
                print(f"{celcius}° son {conversion}° Fahrenheit")

            case 2:
                print("Convertir Fahrenheit a Celcius\n")
                fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
                conversion = (fahrenheit - 32) * 5 / 9
                print(f"{fahrenheit}° son {conversion}° celcius")

            case 0:
                print("Saliendo....")
                break

            case _:
                print("Opcion ingresada es incorrecta...")

def ejercicio10EstudiantesAprobados():
    # 10. Tienes una lista de calificaciones. Crea una lista vacía llamada aprobados = [].
    # Recorre la lista original con un for; si la calificación es mayor o igual a 70, agrégala a la lista de aprobados usando .append().
    # Al terminar el ciclo, imprime la lista de aprobados y muestra cuántos alumnos pasaron usando la función len().

    notas = [55, 80, 92, 45, 75, 66]
    aprobados = []

    print("Ejercicio 10 - Filtro de Estudiantes Aprobados")

    for nota in notas:
        if nota >= 70:
            aprobados.append(nota)

    print(f"Lista de aprobados: {aprobados}")

    print(f"La cantidad de aprobados es: {len(aprobados)}")