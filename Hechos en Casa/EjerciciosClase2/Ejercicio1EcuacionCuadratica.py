import math
from cmath import sqrt

#ax^2+bx+C = 0
#delta = -b^2 - 4ac / 2a
#x = -b +- √delta


#HACER QUE CAPTURE LOS ERRORES POSBILES INECUACIONES, 0 EN a, y todo lo demas, con if anidados

print("Ingrese la ecuacion: \n")

a = int(input("Ingrese a = "))

b = int(input("Ingrese b = "))

c = int(input("Ingrese c = "))

print(f"Su ecuacion queda asi = {a}x^2 + {b}x {c} = 0")

delta = pow(-b, 2) - 4 * a * c

if delta > 0:

    x1 = (-b + delta**0.5) / (2 * a)

    x2 = (-b + delta**0.5) / (2 * a)

    print(f"x1 = {x1}")

    print(f"x2 = {x2}")

if delta < 0:
    parteReal = -b / (2*a)
    parteImaginaria = abs(delta)**0.5 / 2 * a

    print(f"x1 = {parteReal} + {parteImaginaria}i")
    print(f"x2 = {parteReal} - {parteImaginaria}i")