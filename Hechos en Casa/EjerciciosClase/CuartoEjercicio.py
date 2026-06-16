def ejercicio04():

    print("\nPEDIR 4 NOTAS Y SI UNA ES 0 PEDIR AL USUARIO QUE INGRESE NUEVAMENTE")

    n = [0, 0, 0, 0]
    suma = 0
    prom = 0.0

    for i in range(4):
        n[i] = float(input(f"Nota {i + 1}: "))

        while n[i] == 0:
            print("No se puede ingresar una nota con valor de 0. Ingrese nuevamente la nota.")
            n[i] = float(input(f"Nota {i + 1}: "))

        suma += n[i]

    prom = suma / 4
    print(f"\nEl promedio de las 4 notas es = {prom}%")