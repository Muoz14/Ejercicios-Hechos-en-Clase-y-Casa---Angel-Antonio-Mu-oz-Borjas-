from Clases.EcuacionCubica import Cubica
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("--- PRUEBA DE CASOS ---")

print("\n1. Probando Error:")
prueba_error = Cubica(0, 0, 0, 5)
prueba_error.resolver()

print("\n2. Probando Lineal:")
prueba_lineal = Cubica(0, 0, 2, -4)
prueba_lineal.resolver()

print("\n3. Probando Cuadrática (Raíces Complejas):")
prueba_cuadratica = Cubica(0, 1, 0, 1)
prueba_cuadratica.resolver()

print("\n4. Probando Cúbica:")
prueba_cubica = Cubica(1, 1, 0, 1)
prueba_cubica.resolver()