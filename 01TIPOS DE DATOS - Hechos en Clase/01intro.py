import pandas as pd
import os
from array import array

os.system('cls' if os.name == 'nt' else 'clear')

#Arreglo - Son los primitivos, los primeros en aparecer
edades = array("i", [18, 19, 20, 18])

#Lista la diferencia es que no pueden mutar
estudiantes = ["Carlos", "Ana", "Luis", "Maria"]

#Diccionario
notas = {
    "Carlos": 85,
    "Ana": 92,
    "Luis": 78,
    "Maria": 90
}

print(notas["Ana"])

print("Lista de Estudiantes")
print(estudiantes)

print("\nDiccionario de notas")
print(notas)

print("\nArreglo de Edades")
print(edades)

print("\nRecorrido de Datos")

for i in range(len(estudiantes)):
    nombre = estudiantes[i]
    nota = notas[nombre]
    edad = edades[i]

    print(f"Estudiante: {nombre} | Edad: {edad} | Nota: {nota}")

print("\nAGREGANDO NUEVO ESTUDIANTE")    

estudiantes.append("Pedro")
notas["Pedro"] = 88
edades.append(21)

for i in range(len(estudiantes)):
    nombre = estudiantes[i]
    nota = notas[nombre]
    edad = edades[i]

    print(f"Estudiante: {nombre} | Edad: {edad} | Nota: {nota}")

pandas_df = pd.DataFrame({
    "Nota": notas.values()
})

print("\nDATAFRAME SOLO CON NOTAS")
print(pandas_df)