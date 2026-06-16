def ejercicios03():
    # Ciclos

    print("\nCiclos FOR")

    print("\nImprimir 5 numeros de un rango")
    for i in range(5):
        print(i)

    print("\nImprimir numeros pares")
    for i in range(0, 10, 2):
        print(i)

    print("\nImprimir partes y longitud de una cadena")
    cadena = "python"

    for index, letra in enumerate(cadena):
        print(f"Indice: {index}, Letra: {letra}")
        longitud = index + 1

    print("Longitud de la cadena: " + str(longitud))

    print("\nImprimir arreglos")
    arreglo = [12, 22, 32, 42, 52]
    for numero in arreglo:
        print(numero)

    arregloFrutas = ["Manzanas", "Peras", "Piñas", "Sandias"]
    for item in arregloFrutas:
        print(item)