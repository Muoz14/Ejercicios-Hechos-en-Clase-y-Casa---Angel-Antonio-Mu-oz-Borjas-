def ejercicio05():

    print("\nPEDIR UN NUMERO Y MOSTRAR SU FACTORIAL")

    f = 1

    n = int(input("Ingrese el numero del cual quiera visualizar su factorial: "))

    for i in range(1, n + 1):
        f *= i

    print(f"El factorial del numero es = {f}")