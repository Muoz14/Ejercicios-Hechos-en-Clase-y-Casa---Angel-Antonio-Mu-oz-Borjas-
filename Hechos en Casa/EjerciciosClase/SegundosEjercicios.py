def ejercicio02():
    # Promedio de 4 notas
    notas = []
    suma = 0
    prom = 0.0
    error = False

    print("\nPEDIR 4 NOTAS Y SI UNA ES 0 NO GENERAR EL PROMEDIO")

    for i in range(4):
        notas[i] = float(input(f"Nota {i + 1}: "))

        if notas[i] == 0:
            print("No se puede generar el promedio")
            error = True
            break
        else:
            suma += notas[i]

    prom = suma / 4

    if not error:
        print(f"\nEl promedio de las 4 notas es = {prom}%")


