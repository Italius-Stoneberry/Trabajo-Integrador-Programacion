import csv
import os

def validar_existencia(Pais, lista_info_paises):
    if Pais not in lista_info_paises:
        return True
    else:
        return False
#quite el menu de aca porque lo puse en Funciones_de_prueba.py
def cargar_pais(lista_paises,Paises_data):

    while True:
    
        pais=validar_Nombre("Ingrese el nombre del pais: ")
        Existencia=validar_existencia(pais,lista_paises)
        if Existencia:
            print("Nombre guardado correctamente")
        else:
            print("Este país ya existe en el archivo. Intente con otro.")
        break
    
    Poblacion=validar_entero("Ingrese el número de población: ", "Población")
    Superficie=validar_entero("Ingrese el número de superfície en km^2: ","Superfície")
    Continente=validar_Nombre("Ingrese el nombre del Continente al que el país pertenece: ")
    pais_diccionario={
        "País": pais,
        "Población":Poblacion,
        "Superfície":Superficie,
        "Continente":Continente
    }
    lista_paises.append(pais_diccionario)
    if guardar_cambios(Paises_data, lista_paises):
        print("Los datos se guardaron con éxito")
    else:
        print("Los datos no se guardaron, debido al error al momento de cargar")

#quite el listar paises de aca porque lo puse en Funciones_de_prueba.py
# quite el buscar pais de aca porque lo puse en Funciones_de_prueba.py
