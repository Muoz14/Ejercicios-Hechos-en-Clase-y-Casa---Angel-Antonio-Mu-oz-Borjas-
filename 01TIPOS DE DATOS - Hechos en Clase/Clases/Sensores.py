class Sensores:

    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def verificacion(self):

        lista = [self.s1, self.s2, self.s3, self.s4]
        cantidadE = 0
        cantidadA = 0
        activos = []
        conError = []

        for i in lista:
            if i:
                cantidadE += 1
                conError.append("Sensor " + str(i+1) + " activo")
            else:
                cantidadA += 1
                activos.append(i)
    
        print(f"Hay {cantidadE} sensores en falla")

        if cantidadE == 1:
            print("Falla leve")
        elif cantidadE == 2:
            print("Falla indeterminada")
        elif cantidadE == 3:
            print("Falla parcial")
        elif cantidadE == 4:
            print("Falla Grave")    
        else:
            print("Algo aslio mal")
