import numpy as np

class Cubica:

    # Constructor
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    # Función principal para evaluar y resolver
    def resolver(self):
        
        # 1. Validación de Error: No hay variables (a=0, b=0, c=0)
        if self.a == 0 and self.b == 0 and self.c == 0:
            print("Error: Todos los coeficientes de las variables son 0. No es una ecuación válida.")

        # 2. Es una ecuación Lineal (a=0 y b=0, pero c no es 0)
        elif self.a == 0 and self.b == 0:
            print("Es una ecuación lineal")
            # La ecuación es cx + d = 0
            x = -self.d / self.c
            print(f"x = {x}")

        # 3. Es una ecuación Cuadrática (a=0, pero b no es 0)
        elif self.a == 0:
            print("Es una ecuación cuadrática")
            # La ecuación es bx^2 + cx + d = 0
            # Calculamos el delta (discriminante) adaptando las variables
            delta = self.c**2 - 4 * self.b * self.d

            if delta > 0:
                x1 = (-self.c + (delta**0.5)) / (2 * self.b)
                x2 = (-self.c - (delta**0.5)) / (2 * self.b)
                print(f"x1 = {x1}")
                print(f"x2 = {x2}")
            elif delta == 0:
                x = -self.c / (2 * self.b)
                print(f"x1 = x2 = {x}")
            else:
                # Parte real e imaginaria separada
                parteReal = -self.c / (2 * self.b)
                parteCompleja = abs(delta)**0.5 / (2 * self.b)
                print(f"x1 = {parteReal} + {parteCompleja}i")
                print(f"x2 = {parteReal} - {parteCompleja}i")

        # 4. Es una ecuación Cúbica (a no es 0)
        else:
            print("Es una ecuación cúbica")
            # Usamos numpy para extraer las raíces cúbicas con precisión matemática
            coeficientes = [self.a, self.b, self.c, self.d]
            raices = np.roots(coeficientes)

            # Recorremos cada raíz generada para imprimirla con su parte imaginaria
            for i in range(len(raices)):
                raiz = raices[i]
                # Redondeamos a 4 decimales para mayor legibilidad
                parteReal = np.round(raiz.real, 4)
                parteCompleja = np.round(raiz.imag, 4)

                if parteCompleja == 0:
                    # Si no hay parte imaginaria, es una raíz real pura
                    print(f"x{i+1} = {parteReal}")
                elif parteCompleja > 0:
                    # Raíz compleja con signo positivo
                    print(f"x{i+1} = {parteReal} + {parteCompleja}i")
                else:
                    # Raíz compleja con signo negativo (usamos abs() para evitar el choque de signos + -)
                    print(f"x{i+1} = {parteReal} - {abs(parteCompleja)}i")