from Clases.Cuadratica import Cuadratica
import numpy as np

import os
os.system('cls' if os.name == 'nt' else 'clear')

#z = Cuadratica(-1, -1, -1)
#z.raices()

#Ecuacion Cuadratica
print("\nEcuacion Cuadratica\n")
respuesta = np.roots([1,0,1])
print(respuesta)

print(f"x1 = {np.round(respuesta[0], 3)} \nx2 = {np.round(respuesta[1], 20)}\n")


#Ecuacion Cubica
print("\nEcuacion Cubica\n\n")
cubica = np.roots([1, 1, 0, 1])
print(cubica)
print(f"x1 = {np.round(cubica[0], 3)} \nx2 = {np.round(cubica[1], 20)} \nx3 = {np.round(cubica[2], 20)}")


