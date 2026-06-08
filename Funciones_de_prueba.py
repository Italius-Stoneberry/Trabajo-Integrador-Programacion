import csv
import os

carpeta_de_trabajo = os.path.dirname(os.path.abspath(__file__))
ruta_global_archivo = os.path.join(carpeta_de_trabajo, "Paises_data.csv")

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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
    print(f"║{' [4] Ordenamiento':<70}║")
    print(f"║{' [5] Filtros':<70}║")
    print(f"║{' [6] Estadísticas':<70}║")
    print("╠"+"═" * ancho + "╣")
    print(f"║{' [7] Salir':<70}║")
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
                        print("╔"+"═" *80+"╗")
                        print(f"║{'ERROR: {e}, el progrmama no se cerrara, el error será solucionado':^80} ║")
                        print("╚"+"═" *80+"╝")
                        pais["población"] = 0
                        pais["superficie"] = 0.0
                return paises_lista #retorna la lista de diccionarios.
        else:
            print("╔"+"═" *80+"╗")
            print(f"║{'El archivo no fue encontrado, estamos creando una lista vacía para que puedas trabajar.':^80} ║")
            print("╚"+"═" *80+"╝")
            return[]
    except PermissionError:
        print("╔"+"═" *80+"╗")
        print(f"║{'ERROR: El archivo esta abierto en otro programa, cierrelo. O no tienes el permiso para usarlo.':^80} ║")
        print("╚"+"═" *80+"╝")
        return []
    except Exception as Error:
        print("╔"+"═" *80+"╗")
        print(f"║{'OCURRIÓ UN ERROR INESPERADO: {Error}':^80} ║")
        print("╚"+"═" *80+"╝")


def guardar_cambios():
    #La lista_paises_info, es la lista que nos retorna la función cargar_datos, que es guardada en una variable en el main
    if not paises_lista:
        print("╔"+"═" *50+"╗")
        print(f"║{'No hay datos en la lista, el archivo no se actualizará.':^50} ║")
        print("╚"+"═" *50+"╝")
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
        print("╔"+"═" *80+"╗")
        print(f"║{'ERROR: El archivo esta abierto en otro programa, cierrelo e intente nuevamente.':^80} ║")
        print("╚"+"═" *80+"╝")
        return False
    except KeyError:
        print("╔"+"═" *80+"╗")
        print(f"║{'ERROR: Algún elemento de tu archivo está incompleto, FALTA UNA COLUMNA':^80} ║")
        print("╚"+"═" *80+"╝")
        return False
    except Exception as Error:
        print("╔"+"═" *80+"╗")
        print(f"║{'OCURRIÓ UN ERROR INESPERADO: Al querer guardadar datos: {Error}':^80} ║")
        print("╚"+"═" *80+"╝")
        return False
class Longitud_Error(Exception):
    pass
class Error_de_Cantidad(Exception):
    pass
class Error_Repeticion(Exception):
    pass
class nombre_Error(Exception):
    pass
class Rango_Error(Exception):
    pass

def validar_nombre(mensaje):
    while True:
        
        try:
            
            print("╔" + "═" * 80 + "╗")     
            print(f"║{mensaje:<79} ║")
            print("╚" + "═" * 80 + "╝")
            nombre=input(f"\033[2A\033[{len(mensaje)+1}C").strip().capitalize()
            print("\033[1B", end="")
            if len(nombre)<=1 or nombre=="":
                raise Longitud_Error(f"El nombre ingresado debe tener como mínimo 2 caracteres.")
            if not nombre.replace(" ","").isalpha():
                raise nombre_Error(f"El nombre ingresado solo debe contener letras.")
            else:
               return str(nombre)
        except Longitud_Error as e:
            limpiar_pantalla()
            print("╔"+"═" *80+"╗")
            print(f"║{f'ERROR: {e}':^79} ║")
            print("╚"+"═" *80+"╝")
        
        except nombre_Error as e:
            limpiar_pantalla()
            print("╔"+"═" *80+"╗")
            print(f"║{f'ERROR: {e}':^79} ║")
            print("╚"+"═" *80+"╝")

def validar_numero(mensaje_1,mensaje_2, Conjunto_numerico=int):
    tipo='Entero' if Conjunto_numerico==int else 'Decimal'
    while True:
        try:
            print("╔"+"═" *80+"╗")
            print(f"║{mensaje_1:<79} ║")
            print("╚" + "═" * 80 + "╝")
            Numero=Conjunto_numerico(input(f"\033[2A\033[{len(mensaje_1)+1}C").strip())
            print("\033[1B", end="")
            if Numero<=0:
                raise Error_de_Cantidad(f"El número ingresado no es acorde a la {mensaje_2}.")
            else:
                return Numero
        except TypeError:
            limpiar_pantalla()
            print("╔"+"═" *80+"╗")
            print(f"║{f'Error: Debe ingresar un número de tipo {tipo}.':^79} ║")
            print("╚"+"═" *80+"╝")
            continue
        except ValueError:
            limpiar_pantalla()
            print("╔"+"═" *80+"╗")
            print(f"║{f'Error: Debe ingresar un número de tipo {tipo}.':^79} ║")
            print("╚"+"═" *80+"╝")
            continue
        except Error_de_Cantidad as e:
            limpiar_pantalla()
            print("╔"+"═" *80+"╗")
            print(f"║{f'ERROR:{e}':^79} ║")
            print("╚"+"═" *80+"╝")
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
            limpiar_pantalla()
            print("╔" + "═" * 80 + "╗")
            print(f"║{f'ERROR:{e}':^79} ║")
            print("╚" + "═" * 80 + "╝")   
            continue
        except Exception as E:
            print(f"Ocurrió un error Inesperado: {E}")
            continue


def validar_continente(mensaje="Ingrese el continente al cual pertence el país: "):
    continentes=["Europa","América","África","Asia","Oceanía","Antártida"]
    while True:
        try:
            continente=validar_nombre(mensaje)
            if continente not in continentes:
                raise nombre_Error("El nombre del continente ingresado es incorrecto.")
            else:
                return continente
        except nombre_Error as e:
            limpiar_pantalla()
            print("╔" + "═" * 80 + "╗")
            print(f"║{f'ERROR:{e}':^79} ║")
            print("╚" + "═" * 80 + "╝")   
            continue
def validar_existencia(Pais,paises_lista):
    for pais in paises_lista:
        if pais["nombre"]==Pais:
            return True #retorna True solo si existe
    return False #Acá nos va a retornar falses solo si no existe


def listar_pais(lista=None):#le agregué ese parámetro para poder listar la info de los piases sea cual sea la lista
    
    if lista is None:
        lista=paises_lista
    print("╔"+"═" *16+"╦"+"═" *18+"╦"+"═" *17+"╦"+"═" *16+"╗")
    print(f"║{' País ':^16}║{'población':^18}║{'superficie':^17}║{'continente':^16}║")

    if len(lista) == 0:
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")
        print(f"║{"No hay paises cargados":^70}║")
        print("╠"+"═" *70+"╣")

    else:
        print("╠"+"═" *16+"╬"+"═" *18+"╬"+"═" *17+"╬"+"═" *16+"╣")
        for i in range(len(lista)):
            print(f"║{lista[i]["nombre"].title():^16}║{lista[i]["población"]:^18}║{lista[i]["superficie"]:^17}║{lista[i]["continente"].title():^16}║")
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")

    print(f"║{"Oprima ENTER para continuar":^70}║")
    print("╚"+"═"*70+"╝")
    confirm=input("")
    limpiar_pantalla()
    confirm=""


def buscar_pais(): #modifique acá ya que no tiene que recibir parametros, antes estaba así: def buscar_pais(lista_paises):
    #creamos dos listitas
    busqueda=[]
    indice=0
    #seek=input("Que pais estas buscando?\n").lower()
    seek=validar_nombre("Que pais estas buscando? ")
    limpiar_pantalla()

    for pais in paises_lista:
            nombre_pais = pais["nombre"].capitalize()#cambie lower por capitalize()

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
    limpiar_pantalla()
    confirm=""



def validar_opcion(lista,mensaje):
    while True:
        print("╔" + "═" * 70 + "╗")
        print(f"║{mensaje:<69} ║")
        print("╚" + "═" * 70 + "╝")
        op= input(f"\033[2A\033[{len(mensaje)+1}C").strip()
        print("\033[1B", end="")
        if op  in lista:
            return op
        else:
            print("╔" + "═" * 70 + "╗")
            print(f"║{'Intente Nuevamente':^69} ║")
            print("╚" + "═" * 70 + "╝")
    


def seleccion_criterio_ordenamiento():
    while True:
        print("╔"+"═" *70+"╗")
        print(f"║{' CRITERIOS DE ORDENAMIENTO DE LOS PAISES ':^70}║")
        print("╠"+"═" *70+"╣")
        print(f"║{'[1] Nombre':^70}║")
        print(f"║{'[2] Población':^70}║")
        print(f"║{'[3] Superficie':^70}║")
        print("╚"+"═" *70+"╝")
        
        criterio=validar_opcion(["1","2","3"],"Ordenar países por (ingrese número): ")
            
        match criterio:
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
    limpiar_pantalla()
    while True:
        print("╔" + "═" * 70 + "╗")
        print(f"║{'ORDEN DE LA VISUALIZACIÓN':^69} ║")
        print("╠" + "═" * 70 + "╣")
        print(f"║{'[1] Ascendente (Menor a Mayor / A-Z)':^69} ║")
        print(f"║{'[2] Descendente (Mayor a Menor / Z-A)':^69} ║")
        print("╚" + "═" * 70 + "╝")
        orden=validar_opcion(["1","2"],"Seleccione el orden en el que desea ordenar la lista: ")
           
        match orden:
            case "1":
                Ascendete= False
                return Ascendete
            case "2":
                Descendente=True
                return Descendente


def ordenamiento():
    global paises_lista
    Criterio=seleccion_criterio_ordenamiento()
    Orden=elección_orden()
    lista_Ordenada=sorted(paises_lista, key=lambda x: x[Criterio], reverse=Orden)
    mostrar_lista_ordenada(lista_Ordenada,Criterio,Orden)


def mostrar_lista_ordenada(lista, criterio, Orden):
    limpiar_pantalla()
    if Orden== False :
        Ordenada= "Ascendente" 
    else:
        Ordenada= "Descendente"
    print("╔" + "═" * 70 + "╗")
    print(f"║{'LISTA ORDENADA BAJO EL CRITERIO ' + criterio + ' DE MANERA ' + Ordenada:^69} ║")
    print("╠"+"═" *16+"╦"+"═" *17+"╦"+"═" *17+"╦"+"═" *17+"╣")
    print(f"║{'País':^15} ║ {'población':^15} ║ {'superficie':^15} ║ {'continente':^15} ║")
    print("╠"+"═" *16+"╬"+"═" *17+"╬"+"═" *17+"╬"+"═" *17+"╣")
    for pais in lista:
     print(f"║{pais['nombre'].capitalize():^15} ║ {pais['población']:^15} ║ {pais['superficie']:^15} ║ {pais['continente'].capitalize():^15} ║")   
    print("╠"+"═" *16+"╩"+"═" *17+"╩"+"═" *17+"╩"+"═" *17+"╣")
    print(f"║{'Presione ENTER para continuar':^69} ║")
    print("╚" + "═" * 70 + "╝")
    confirm=input("")
    limpiar_pantalla()


def filtrar_paises():
    limpiar_pantalla()
    print("╔" + "═" * 70 + "╗")
    print(f"║{'FILTRADO DE PAÍSES':^69} ║")
    print("╠" + "═" * 70 + "╣")
    print(f"║{'[1]-POR CONTINENTE':^69} ║")
    print(f"║{'[2]-POR RANGO DE POBLACIÓN':^69} ║")
    print(f"║{'[3]-POR RANGO DE SUPERFÍCIE':^69} ║")
    print("╚" + "═" * 70 + "╝")
    filtro=validar_opcion(["1","2","3"],"Seleccione una opción de filtrado (1,2,3): ")
    match filtro:
        case "1":
            filtro_continentes()
            return
        case "2":
            filtro_rango("Ingrese el valor mínimo de población: ",'población', int)
            return
        case "3":
            filtro_rango("Ingrese el valor mínimo de superficie: ",'superficie', float)
            return 



def filtro_continentes():
    filtrados=[]
    limpiar_pantalla()
    continente=validar_continente("Continente por el cual desea filtrar: ")
    for dato in paises_lista:
        if dato['continente']==continente:
            filtrados.append(dato)
    listar_pais(filtrados)



def validar_rango(mensaje_1,clave,conjunto_numerico):
    valor_minimo=validar_numero(mensaje_1,clave,conjunto_numerico)
    while True:
        try:
            valor_maximo=validar_numero("Ingrese el valor máximo: ",clave,conjunto_numerico)
            if valor_maximo>=valor_minimo:
                return valor_minimo,valor_maximo
            else:
                raise Rango_Error("El valor máximo no puede ser menor al valor mínimo")
        except Rango_Error as e:
            print(f"ERROR: {e}")






def filtro_rango(mensaje_1,clave,conjunto_numerico):
    filtrados_rango=[]
    minimo,maximo=validar_rango(mensaje_1,clave,conjunto_numerico)
    for pais in paises_lista:
        if minimo<=pais[clave]<=maximo:
            filtrados_rango.append(pais)
    listar_pais(filtrados_rango)
    

def estadistica():
    continentes=["Europa","América","África","Asia","Oceanía"]
    print("╔"+"═" *80+"╗")
    print(f"║{' ESTADÍSTICAS DE LOS PAÍSES (cargados)':^79} ║")
    print("╠"+"═" *80+"╣")
    
    
    pais_mayor = max(paises_lista, key=lambda x: x['población'])
    pais_menor = min(paises_lista, key=lambda x: x['población'])
    promedio_poblacion=sum(map(lambda x:x['población'], paises_lista))/len(paises_lista)
    promedio_superficie=sum(map(lambda x:x['superficie'], paises_lista))/len(paises_lista)

    
    texto_mayor = f"País con mayor población: {pais_mayor['nombre']} con {pais_mayor['población']}"
    texto_menor = f"País con menor población: {pais_menor['nombre']} con {pais_menor['población']}"
    texto_promedio_poblacion=f"El promedio de poblacion de todos los paises es de: {promedio_poblacion: .0f} personas"
    texto_promedio_superficie=f"El promedio de superficie de todos los paises es de: {promedio_superficie: .2f} km²"
    
    print(f"║{texto_mayor:<80}║")
    print(f"║{texto_menor:<80}║")
    print(f"║{texto_promedio_poblacion:<80}║")
    print(f"║{texto_promedio_superficie:<80}║")
    print("╚"+"═" *80+"╝")
    print("")


    print("╔" + "═" * 80 + "╗")
    print(f"║{' CANTIDAD DE PAÍSES POR CONTINENTE':^80}║")
    print("╠" + "═" * 80 + "╣")
    
    for continente in continentes:
        # 1. Calculamos la cantidad (es tu misma línea, pero guardada en una variable)
        cantidad = len(list(filter(lambda x: x['continente'] == continente, paises_lista)))
        
        # 2. Armamos el texto limpio
        texto = f" La cantidad de Paises de {continente.capitalize()} en la lista es de: {cantidad}"
        
        # 3. Lo imprimimos forzando a que ocupe 80 espacios hacia la izquierda (<80)
        print(f"║{texto:<80}║")
        
    print("╚" + "═" * 80 + "╝")
    print("\nOprima ENTER para continuar")
    input("")