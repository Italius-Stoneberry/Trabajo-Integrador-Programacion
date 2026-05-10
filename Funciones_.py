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


def mostrar_menu():
    ancho=70
    print("╔"+"═" *ancho+"╗")
    print(f"║{' Hola bienvenido al gestor de paises ':^70}║")
    print("╠"+"═" *ancho+"╣")
    print(f"║{' [1] Agregar pais':<70}║")
    print(f"║{' [2] Listar paises':<70}║")
    print(f"║{' [3] Buscar pais':<70}║")
    print(f"║{' [4] Modificar pais':<70}║")
    print(f"║{' [5] Eliminar':<70}║")
    print("╠"+"═" * ancho + "╣")
    print(f"║{' [6] Salir':<70}║")
    print("╚"+"═" * ancho + "╝")






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

def listar_pais(lista_paises):
    #creamos dos listitas

    print("╔"+"═" *16+"╦"+"═" *18+"╦"+"═" *17+"╦"+"═" *16+"╗")
    print(f"║{' País ':^16}║{'Población':^18}║{'Superfície':^17}║{'Continente':^16}║")

    if len(lista_paises) == 0:
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")
        print(f"║{"No hay paises cargados":^70}║")
        print("╠"+"═" *70+"╣")

    else:
        print("╠"+"═" *16+"╬"+"═" *18+"╬"+"═" *17+"╬"+"═" *16+"╣")
        for i in range(len(lista_paises)):
            print(f"║{lista_paises[i]["País"].title():^16}║{lista_paises[i]["Población"]:^18}║{lista_paises[i]["Superfície"]:^17}║{lista_paises[i]["Continente"].title():^16}║")
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")

    print(f"║{"Oprima ENTER para continuar":^70}║")
    print("╚"+"═"*70+"╝")
    confirm=input("")
    confirm=""




def buscar_pais(lista_paises):
    #creamos dos listitas
    busqueda=[]
    indice=0
    seek=input("Que pais estas buscando?\n").lower()

    for pais in lista_paises:
            nombre_pais = pais["País"].lower()

            if nombre_pais.startswith(seek):
                busqueda.append([pais["País"],pais["Población"],pais["Superfície"],pais["Continente"]])


    print("╔"+"═" *16+"╦"+"═" *18+"╦"+"═" *17+"╦"+"═" *16+"╗")
    print(f"║{' Pais ':^16}║{'Poblacion':^18}║{'Superficie':^17}║{'Continente':^16}║")

    if len(busqueda) == 0:
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")
        print(f"║{"No se encotraron paises con ese nombre":^70}║")
        print("╠"+"═" *70+"╣")

    else:
        print("╠"+"═" *16+"╬"+"═" *18+"╬"+"═" *17+"╬"+"═" *16+"╣")
        for i in range(len(busqueda)):
            print(f"║{busqueda[i][0].title():^16}║{busqueda[i][1]:^18}║{busqueda[i][2]:^17}║{busqueda[i][3].title():^16}║")
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")

        
    print(f"║{"Oprima ENTER para continuar":^70}║")
    print("╚"+"═"*70+"╝")
    confirm=input("")
    confirm=""

