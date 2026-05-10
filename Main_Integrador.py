import csv
import os
import Funciones_
ruta_archivo="Paises_data.csv"
paises=Funciones_.cargar_datos(ruta_archivo)
print("Ingresar datos:")

while True:
    Pais_Nombre=Funciones_.validar_Nombre("Ingrese el nombre del pais: ")
    Existencia=Funciones_.validar_existencia(Pais_Nombre,paises)
    if Existencia:
        print("Nombre guardado correctamente")
    else:
        print("Este país ya existe en el archivo. Intente con otro.")
        break
    Poblacion=Funciones_.validar_entero("Ingrese el número de población: ", "Población")
    Superficie=Funciones_.validar_entero("Ingrese el número de superfície en km^2: ","Superfície")
    Continente=Funciones_.validar_Nombre("Ingrese el nombre del Continente al que el país pertenece: ")
    pais_diccionario={
        "País": Pais_Nombre,
        "Población":Poblacion,
        "Superfície":Superficie,
        "Continente":Continente
    }
    paises.append(pais_diccionario)
    if Funciones_.guardar_cambios(ruta_archivo, paises):
        print("Los datos se guardaron con éxito")
    else:
        print("Los datos no se guardaron, debido al error al momento de cargar")
    break
print(paises)