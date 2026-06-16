class FormulasConversion:

    def __init__(self, g):
        self.g = g

    #Convertir de Grados Celsius a....
    def cGradosFahrenheit(self):
        f = self.g * 1.8 + 32
        print(f"La conversion de grados Celsius a Fahrenheit es = {f}°")

    def cGradosKelvin(self):
        k = self.g + 273.15
        print(f"La conversion de grados Celsius a Kelvin es = {k}°")

    def cGradosRankine(self):
        r = (self.g + 273.15) * 1.8
        print(f"La conversion de grados Celsius a Rankine es = {r}")

    #Convertir de Fahrenheit a....
    def fGradosCelsius(self):
        c = (self.g - 32) / 1.8
        print(f"La conversion de grados Fahrenheit a Celsius es = {c}")

    def fGradosKelvin(self):
        k = (self.g + 459.67) / 1.8
        print(f"La conversion de grados Fahrenheit a Kelvin es = {k}")

    def fGradosRankine(self):
        r = self.g + 459.67
        print(f"La conversion de grados Fahrenheit a Rankine es = {r}")

    #Convertir Kelvin a....
    def kGradosCelsius(self):
        c = self.g - 273.15
        print(f"La conversion de grados Kelvin a Celsius es = {c}")

    def kGradosFahrenheit(self):
        f = (self.g * 9 / 5) - 459.67
        print(f"La conversion de grados Kelvin a Fahrenheit es = {f}")