import csv
import os

carpeta_de_trabajo = os.path.dirname(os.path.abspath(__file__))
ruta_global_archivo = os.path.join(carpeta_de_trabajo, "Paises_data.csv")

#Datos de prueba
paises_lista=[ {"nombre": "Argentina", "población": 45376763, "superficie": 278040.0, "continente": "América"},
    {"nombre": "Japon", "población": 125800000, "superficie": 377975.0, "continente": "Europa"}
]

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



def cargar_datos():
    global paises_lista, ruta_global_archivo
    
    try:
        if os.path.exists(ruta_global_archivo):
            with open(ruta_global_archivo,"r", encoding="utf-8-sig") as Archivo:
                lector=csv.DictReader(Archivo,delimiter=";")
                paises_lista=list(lector)
                for pais in paises_lista:
                    try:
                        pais["población"]=int(pais["población"])
                        pais["superficie"]=float(pais["superficie"])  
                    except (ValueError,KeyError,TypeError) as e:
                        print(f"ERROR: {e}, el progrmama no se cerrara, el error será solucionado")
                        pais["población"] = 0
                        pais["superficie"] = 0.0
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
    Encabezados_Claves=["nombre","población","superficie","continente"]
    try:
        with open(ruta_global_archivo,"w", newline="", encoding="utf-8-sig") as Archivo_Escritura:
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
class nombre_Error(Exception):
    pass


def validar_nombre(mensaje):
    while True:
        try:
            nombre=input(mensaje).strip().capitalize()
            if not nombre.replace(" ","").isalpha():
                print("El nombre ingresado solo debe contener letras.")
                continue
            elif len(nombre)<=1:
                raise Longitud_Error("El nombre ingresado debe tener como mínimo 2 caracteres.")
            else:
               return str(nombre)
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

#Estoy rehaciendo la función de agregar paises para evitar repeticiones
def agregar_paises():
    global paises_lista
    while True:
        try:
            Pais_Nuevo= validar_nombre("Ingrese el nombre del País a agregar: ")
            
            if not validar_existencia(Pais_Nuevo,paises_lista):
                Poblacion_Pais_Nuevo=validar_numero("Ingrese el número de población del nuevo país: ", "población", int)
                superficie_Pais_Nuevo=validar_numero("Ingrese el número de superficie en km^2 para el nuevo país: ","superficie", float)
                Continete_Nuevo_Pais=validar_continente()
                Pais_Nuevo_Dict={
                    "nombre":Pais_Nuevo,
                    "población":Poblacion_Pais_Nuevo,
                    "superficie":superficie_Pais_Nuevo,
                    "continente":Continete_Nuevo_Pais
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
            continente=validar_nombre("Ingrese el continente al cual pertence el país: ")
            if continente not in continentes:
                raise nombre_Error("El nombre del continente ingresado es incorrecto, asegúrese de escribirlo bien.")
            else:
                return continente
        except nombre_Error as e:
            print(f"ERROR: {e}")   
            continue
def validar_existencia(Pais,paises_lista):
    for pais in paises_lista:
        if pais["nombre"]==Pais:
            return True #retorna True solo si existe
    return False #Acá nos va a retornar falses solo si no existe


def listar_pais():
    #creamos dos listitas

    print("╔"+"═" *16+"╦"+"═" *18+"╦"+"═" *17+"╦"+"═" *16+"╗")
    print(f"║{' País ':^16}║{'población':^18}║{'superficie':^17}║{'continente':^16}║")

    if len(paises_lista) == 0:
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")
        print(f"║{"No hay paises cargados":^70}║")
        print("╠"+"═" *70+"╣")

    else:
        print("╠"+"═" *16+"╬"+"═" *18+"╬"+"═" *17+"╬"+"═" *16+"╣")
        for i in range(len(paises_lista)):
            print(f"║{paises_lista[i]["nombre"].title():^16}║{paises_lista[i]["población"]:^18}║{paises_lista[i]["superficie"]:^17}║{paises_lista[i]["continente"].title():^16}║")
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")

    print(f"║{"Oprima ENTER para continuar":^70}║")
    print("╚"+"═"*70+"╝")
    confirm=input("")
    confirm=""


def buscar_pais(): #modifique acá ya que no tiene que recibir paramestros, antes estaba así: def buscar_pais(lista_paises):
    #creamos dos listitas
    busqueda=[]
    indice=0
    seek=input("Que pais estas buscando?\n").lower()

    for pais in paises_lista:
            nombre_pais = pais["nombre"].lower()

            if nombre_pais.startswith(seek):
                busqueda.append([pais["nombre"],pais["población"],pais["superficie"],pais["continente"]])


    print("╔"+"═" *16+"╦"+"═" *18+"╦"+"═" *17+"╦"+"═" *16+"╗")
    print(f"║{' Pais ':^16}║{'Poblacion':^18}║{'superficie':^17}║{'continente':^16}║")

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
#________________________
#parte de joaquin
def seleccion_criterio_ordenamiento():
    while True:
        print("CRITERIOS DE ORDENAMIENTO DE LOS PAISES:\n" \
        "1-nombre\n" \
        "2-población\n" \
        "3-superficie")
        while True:
            criterio= input("Ingrese el número del criterio por el cual desea ordenar los países: ").strip()
            if criterio  in ["1","2","3"]:
                break
            else:
                print("Intente Nuevamente")
        match criterio  :
            case"1":
                criterio="nombre"
                return criterio
            case "2":
                criterio="población"
                return criterio
            case "3":
                criterio="superficie"
                return criterio
def elección_orden():
    while True:
        print("ORDEN DE LA VISUALIZACIÓN\n" \
        "1-Ascendente (Menor a Mayor / A-Z)\n "
        "2-Descendente (Mayor a Menor / Z-A)\n")
        while True:
            orden=input("Ingrese el número correspondiente al orden que desea: ").strip()
            if orden in ["1","2"]:
                break
            else:
                print("Intente Nuevamente")
        match orden:
            case "1":
                Ascendete= False
                return Ascendete
            case "2":
                Descendente=True
                return Descendente


def ordenamiento():
    global paises_lista
    print("Ordenar Países")
    Criterio=seleccion_criterio_ordenamiento()
    Orden=elección_orden()
    lista_Ordenada=sorted(paises_lista, key=lambda x: x[Criterio], reverse=Orden)
    mostrar_lista_ordenada(lista_Ordenada,Criterio,Orden)

def mostrar_lista_ordenada(lista, criterio, Orden):
    Ordenada= "Ascendente" if Orden== False else  "Descendente"
    print(f"Lista Ordenada bajo el criterio '{criterio}' de manera '{Ordenada}'")
    for pais in lista:
     print(f"País: {pais['nombre']:<15} | población: {pais['población']:<12} | superficie: {pais['superficie']} km²")   
#________________________
#parte de italo


