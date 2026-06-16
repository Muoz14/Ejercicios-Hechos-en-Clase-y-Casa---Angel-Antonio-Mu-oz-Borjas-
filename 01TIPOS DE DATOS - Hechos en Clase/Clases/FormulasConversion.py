class FormulasConversion:

    def __init__(self, g):
        self.g = g

    def cGradosFahrenheit(self):
        f = self.g * 1.8 + 32
        print(f"La conversion de grados Celcius a Fahrenheit es = {f}°")

    def cGradosKelvin(self):
        k = self.g + 273.15
        print(f"La conversion de grados Celcius a Kelvin es = {k}°")
            