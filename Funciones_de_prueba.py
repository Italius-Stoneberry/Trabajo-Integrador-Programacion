import csv
import os
ruta_global_archivo="Paises_data.csv"
#Datos de prueba
paises_lista=[ {"País": "Argentina", "Población": 45376763, "Superfície": 2780400, "Continente": "América"},
    {"País": "Japon", "Población": 125800000, "Superfície": 377975, "Continente": "Europa"}
]
def cargar_datos(Paises_data):
    global paises_lista, ruta_archivo
    ruta_archivo=Paises_data
    try:
        if os.path.exists(Paises_data):
            with open(Paises_data,"r", encoding="utf-8-sig") as Archivo:
                lector=csv.DictReader(Archivo,delimiter=";")
                paises_lista=list(lector)
                return paises_lista #retorna la lista de diccionarios.
        else:
            print("El archivo no fue encontrado, estamos creando una lista vacía para que puedas trabajar.")
            return[]
    except PermissionError:
        print("El archivo esta abierto en otro programa, cierrelo. O no tienes el permiso para usarlo.\nEn ambos casos intente nuevamente")
        return []
    except Exception as Error:
        print(f"OCURRIÓ UN ERROR INESPERADO: {Error}")


def guardar_cambios():
    #La lista_paises_info, es la lista que nos retorna la función cargar_datos, que es guardada en una variable en el main
    if not paises_lista:
        print("No hay datos en la lista, el archivo no se actualizará.")
        return False
    Encabezados_Claves=["País","Población","Superfície","Continente"]
    try:
        with open(ruta_archivo,"w", newline="", encoding="utf-8-sig") as Archivo_Escritura:
            #se crea el escritor que actua como un puente entre los datos de la RAM y el Archivo_Escritura
            escritor=csv.DictWriter(Archivo_Escritura,fieldnames=Encabezados_Claves,delimiter=';')
            #se escribe la primera fila en el Archivo_Escritura, la cual representa los encabezados de las columnas
            escritor.writeheader()
            #se va a guardar cada valor contenido en el diccionario en la columna que le corresponde
            escritor.writerows(paises_lista)
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
class Error_Repeticion(Exception):
    pass
class Nombre_Error(Exception):
    pass


def validar_Nombre(mensaje):
    while True:
        try:
            Nombre=input(mensaje).strip().capitalize()
            if not Nombre.replace(" ","").isalpha():
                print("El nombre ingresado solo debe contener letras.")
                continue
            elif len(Nombre)<=1:
                raise Longitud_Error("El nombre ingresado debe tener como mínimo 2 caracteres.")
            else:
               return str(Nombre)
        except Longitud_Error as e:
            print(F"ERROR: {e}")
            continue
def validar_numero(mensaje_1,mensaje_2, Conjunto_numerico=int):
    tipo='Entero' if Conjunto_numerico==int else 'Decimal'
    while True:
        try:
            Numero=Conjunto_numerico(input(mensaje_1))
            if Numero<=0:
                raise Error_de_Cantidad(f"Es probable que el número ingresado no sea acorde a la realidad de la {mensaje_2}.")
            else:
                return Numero
        except TypeError:
            
            print(f"Error: Debe ingresar un número de tipo {tipo}. Intente nuevamente")
            continue
        except ValueError:
             print(f"Error: Debe ingresar un número de tipo {tipo}. Intente nuevamente")
             continue
        except Error_de_Cantidad as e:
            print(f"ERROR:{e}\nIntente nuevamente.")
            continue
#def validar_decimal(mensaje_1,mensaje_2):
#Estoy rehaciendo la función de agregar paises para evitar repeticiones
def agregar_paises():
    global paises_lista
    while True:
        try:
            Pais_Nuevo= validar_Nombre("Ingrese el Nombre del País a agregar: ")
            
            if not validar_existencia(Pais_Nuevo,paises_lista):
                Poblacion_Pais_Nuevo=validar_numero("Ingrese el número de población del nuevo país: ", "Población", int)
                Superficie_Pais_Nuevo=validar_numero("Ingrese el número de superfície en km^2 para el nuevo país: ","Superfície", float)
                Continete_Nuevo_Pais=validar_continente()
                Pais_Nuevo_Dict={
                    "País":Pais_Nuevo,
                    "Población":Poblacion_Pais_Nuevo,
                    "Superfície":Superficie_Pais_Nuevo,
                    "Continente":Continete_Nuevo_Pais
                }
                paises_lista.append(Pais_Nuevo_Dict)
                if guardar_cambios():
                    print(f"El país '{Pais_Nuevo}' y sus datos fueron guardados con éxito")
                else: print("Se produjo un error al guardar los datos.")
                break
                
            else:  
                raise Error_Repeticion("El país ya se encuentra registrado. Prube con otro.")
        except Error_Repeticion as e:
            print(f"ERROR: {e}")
            continue
        except Exception as E:
            print(f"Ocurrió un error Inesperado: {E}")
            continue


def validar_continente():
    continentes=["Europa","América","África","Asia","Oceanía","Antártida"]
    while True:
        try:
            Continente=validar_Nombre("Ingrese el continente al cual pertence el país: ")
            if Continente not in continentes:
                raise Nombre_Error("El nombre de continente ingresado es incorrecto, asegúrese de escribirlo bien.")
            else:
                return Continente
        except Nombre_Error as e:
            print(f"ERROR: {e}")   
            continue
def validar_existencia(Pais,paises_lista):
    for pais in paises_lista:
        if pais["País"]==Pais:
            return True #retorna True solo si existe
    return False #Acá nos va a retornar falses solo si no existe