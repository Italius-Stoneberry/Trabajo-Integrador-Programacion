import csv
import os
import Funciones_ as fun
ruta_archivo="Paises_data.csv"
paises=fun.cargar_datos(ruta_archivo)
import Funciones_de_prueba
ruta_archivo="Paises_data.csv"
Funciones_de_prueba.cargar_datos("Paises_data.csv")


'''while True:
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
    Poblacion=Funciones_.validar_numero("Ingrese el número de población: ", "Población", int)
    Superficie=Funciones_.validar_numero("Ingrese el número de superfície en km^2: ","Superfície", float)
    Continente=Funciones_.validar_Nombre("Ingrese el nombre del Continente al que el país pertenece: ")
    pais_diccionario={
        "País": Pais_Nombre,
        "Población":Poblacion,
        "Superfície":Superficie,
        "Continente":Continente
    }
    paises.append(pais_diccionario)'''
#Estoy simulando un main, lo que estar arriab entre las comillas comentado, podés borrarlo
while True:
    print("\n--- MENÚ DE GESTIÓN DE PAÍSES ---")
    print("1. Agregar País")
    print("2. Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        Funciones_de_prueba.agregar_paises() # No le pasamos nada, ella ya sabe qué hacer
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")
if  Funciones_de_prueba.guardar_cambios():
        print("Los datos se guardaron con éxito")
else:
        print("Los datos no se guardaron, debido al error al momento de cargar")