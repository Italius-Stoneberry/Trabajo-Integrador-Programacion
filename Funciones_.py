import csv
import os
def cargar_datos(Paises_data):
    try:
        if os.path.exists(Paises_data):
            with open(Paises_data,"r", encoding="utf-8-sig") as Archivo:
                lector=csv.DictReader(Archivo,delimiter=";")
                return list(lector) #retorna la lista de diccionarios.
        else:
            print("El archivo no fue encontrado, estamos creando una lista vacía para que puedas trabajar.")
            return[]
    except PermissionError:
        print("El archivo esta abierto en otro programa, cierrelo. O no tienes el permiso para usarlo.\nEn ambos casos intente nuevamente")
        return None
    except Exception as Error:
        print(f"OCURRIÓ UN ERROR INESPERADO: {Error}")


def guardar_cambios(Paises_data, lista_pasies_info):
    #La lista_paises_info, es la lista que nos retorna la función cargar_datos, que es guardada en una variable en el main
    if not lista_pasies_info:
        print("No hay datos en la lista, el archivo no se actualizará.")
        return False
    Encabezados_Claves=["País","Población","Superfície","Continente"]
    try:
        with open(Paises_data,"w", newline="", encoding="utf-8-sig") as Archivo_Escritura:
            #se crea el escritor que actua como un puente entre los datos de la RAM y el Archivo_Escritura
            escritor=csv.DictWriter(Archivo_Escritura,fieldnames=Encabezados_Claves,delimiter=';')
            #se escribe la primera fila en el Archivo_Escritura, la cual representa los encabezados de las columnas
            escritor.writeheader()
            #se va a guardar cada valor contenido en el diccionario en la columna que le corresponde
            escritor.writerows(lista_pasies_info)
            return True
    except PermissionError:
        print("ERROR: El archivo esta abierto en otro programa, cierrelo e intente nuevamente.")
        return False
    except KeyError:
        print("ERROR: Algún elemento de tu archivo está incompleto 'FALTA UNA COLUMNA'")
        return False
    except Exception as Error:
        print(f"OCURRIÓ UN ERROR INESPERADO: Al querer guardadar datos: {Error}")
        return False
class Longitud_Error(Exception):
    pass
class Error_de_Cantidad(Exception):
    pass


def validar_Nombre(mensaje):
    while True:
        try:
            Nombre=input(mensaje).strip().capitalize()
            if not Nombre.isalpha():
                print("El nombre ingresado solo debe contener letras.")
                continue
            elif len(Nombre)<=1:
                raise Longitud_Error("El nombre ingresado debe tener como mínimo 2 caracteres.")
            else:
               return str(Nombre)
        except Longitud_Error as e:
            print(F"ERROR: {e}")
            continue
def validar_entero(mensaje_1,mensaje_2):
    while True:
        try:
            Entero=int(input(mensaje_1))
            if Entero<=0:
                raise Error_de_Cantidad(f"Es probable que el número ingresado no sea acorde a la realidad de la {mensaje_2}.")
            else:
                return Entero
        except TypeError:
            print("Error: Debe ingresar un número de tipo entero. Intente nuevamente")
            continue
        except ValueError:
             print("Error: Debe ingresar un número de tipo entero. Intente nuevamente")
            
        except Error_de_Cantidad as e:
            print(f"ERROR:{e}\nIntente nuevamente.")
            continue
def validar_existencia(Pais, lista_info_paises):
    if Pais not in lista_info_paises:
        return True
    else:
        return False