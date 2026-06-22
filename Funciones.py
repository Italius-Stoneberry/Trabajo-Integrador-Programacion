import csv
import os

carpeta_de_trabajo = os.path.dirname(os.path.abspath(__file__))
ruta_global_archivo = os.path.join(carpeta_de_trabajo, "Paises_data.csv")

"""
Funcion limpiar_pantalla, no recibe parametro
Limpia la pantalla.
"""
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
paises_lista = []

"""
Funcion mostrar_menu, no recibe parametro
Muestra el menu de opciones.
"""
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


archivo_roto= False

"""
Funcion mensaje_bloqueo_de_seguridad, no recibe parametro
Muestra un mensaje de error cuando el archivo esta corrupto o no se puede acceder a el.
"""
def mensaje_bloqueo_de_seguridad():
    print("╔" + "═" * 80 + "╗")
    print(f"║{' ERROR DE SISTEMA ':^80}║")
    print("╠" + "═" * 80 + "╣")
    print(f"║{'No es posible acceder y/o procesar el archivo CSV de forma segura.':^80}║")
    print(f"║{'Revise nombre de las columnas o si el archivo está abierto en otro lado.':^80}║")
    print(f"║{'evise y arrgele el CSV así puede operar con el.':^80}║")
    print(f"║{'El guardado de datos se canceló para evitar perder información.':^80}║")
    print("╚" + "═" * 80 + "╝")

"""
Funcion cargar_datos, no recibe parametro
Carga los datos del archivo CSV a la lista de diccionarios.
"""
def cargar_datos():
    global paises_lista, ruta_global_archivo, archivo_roto
    paises_lista=[]
    try:
        if os.path.exists(ruta_global_archivo):
            
            errores_encontrados=0
            with open(ruta_global_archivo,"r", encoding="utf-8-sig") as Archivo:
                lector=csv.DictReader(Archivo,delimiter=";")
                
                columnas_esperadas = {"nombre", "población", "superficie", "continente"}

                
                if lector.fieldnames is None or not columnas_esperadas.issubset(lector.fieldnames):
                 archivo_roto = True
                 print("╔"+"═" *80+"╗")
                 print(f"║{'ERROR CRÍTICO: Las columnas del CSV fueron modificadas o eliminadas.':^80}║")
                 print(f"║{'Se bloqueará el guardado de datos para evitar que pierda su información.':^80}║")
                 print("╚"+"═" *80+"╝")
                 return []
                paises_lista=list(lector)
                for pais in paises_lista:
                    try:
                        pais["población"]=int(pais["población"])
                        pais["superficie"]=float(pais["superficie"])  
                    except (ValueError,TypeError):
                        errores_encontrados+=1
                        pais["población"] = 0
                        pais["superficie"] = 0.0
                if errores_encontrados>0 and not archivo_roto:
                    print("╔"+"═" *80+"╗")
                    print(f"║{'AVISO: Se encontraron errores en ' + str(errores_encontrados) + ' filas.':^80}║")
                    print(f"║{'El error se produjo porque agregaron un valor no numérico desde el CSV.':^80}║")
                    print(f"║{'Verifique en las casillas "población" y "superficie".':^80}║")
                    print(f"║{'Dichas casillas tendran el valor nuérico "0".':^80}║")
                    print("╚"+"═" *80+"╝")
                    guardar_cambios()
                return paises_lista
        else:
            print("╔"+"═" *80+"╗")
            print(f"║{'El archivo no fue encontrado, estamos creando una lista vacía para que puedas trabajar.':^80} ║")
            print("╚"+"═" *80+"╝")
            return[]
    except PermissionError:
        archivo_roto=True
        print("╔"+"═" *80+"╗")
        print(f"║{'ERROR: El archivo está abierto en otro programa, ciérrelo. O no tienes el permiso para usarlo.':^80} ║")
        print("╚"+"═" *80+"╝")
        return []
    except KeyError as e:
        limpiar_pantalla()
        archivo_roto = True
        print("╔" + "═" * 80 + "╗")
        print(f"║{' ERROR EN LA ESTRUCTURA DEL ARCHIVO ':^80}║")
        print("╠" + "═" * 80 + "╣")
        print(f"║{'No se pudo leer la columna:':^80}║")
        print(f"║{str(e):^80}║")
        print(f"║{'El archivo CSV tiene un formato incompatible o está corrupto.':^80}║")
        print(f"║{'Por favor, repare el archivo antes de continuar.':^80}║")
        print("╚" + "═" * 80 + "╝")
        return []
    except Exception as Error:
        archivo_roto=True
        print("╔"+"═" *80+"╗")
        print(f"║{f'OCURRIÓ UN ERROR INESPERADO: {Error}':^80} ║")
        print("╚"+"═" *80+"╝")


"""
Funcion guardar_cambios, no recibe parametro
Guarda los cambios en el archivo CSV.
"""
def guardar_cambios():
    global archivo_roto
    if archivo_roto:
        mensaje_bloqueo_de_seguridad()
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
        print(f"║{'ERROR:El archivo esta abierto en otro programa, cierrelo e intente nuevamente.':^79} ║")
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
"""
Funcion validar_nombre, recibe como parametro un mensaje
Solicita al usuario que ingrese un nombre y lo valida.
"""
def validar_nombre(mensaje):
    while True:
        
        try:
            
            print("╔" + "═" * 80 + "╗")     
            print(f"║{mensaje:<79} ║")
            print("╚" + "═" * 80 + "╝")
            nombre=input(f"\033[2A\033[{len(mensaje)+1}C").strip().title()
            print("\033[1B", end="")
            if len(nombre)<=1 or nombre=="":
                raise Longitud_Error(f"El nombre ingresado debe tener como mínimo 2 caracteres.")
            if not nombre.replace(" ","").replace("-","").isalpha():
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
"""
Funcion validar_numero, recibe como parametro un mensaje, otro mensaje y un tipo numerico
Solicita al usuario que ingrese un número, validandolo y retornandolo.
"""
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
"""
Funcion agregar_paises, no recibe parametro
Solicita al usuario que ingrese un pais y sus datos, validandolos y guardandolos en la lista de paises.
"""
def agregar_paises():
    global paises_lista
    while True:
        try:
            Pais_Nuevo= validar_nombre("Ingrese el nombre del País a agregar: ")
            
            if not validar_existencia(Pais_Nuevo,paises_lista):
                Poblacion_Pais_Nuevo=validar_numero("Ingrese el número de población del nuevo país: ", "población", int)
                superficie_Pais_Nuevo=validar_numero("Ingrese el número de superficie en km^2 para el nuevo país: ","superficie", float)
                Continente_Nuevo_Pais=validar_continente()
                Pais_Nuevo_Dict={
                    "nombre":Pais_Nuevo,
                    "población":Poblacion_Pais_Nuevo,
                    "superficie":superficie_Pais_Nuevo,
                    "continente":Continente_Nuevo_Pais
                }
                paises_lista.append(Pais_Nuevo_Dict)
                if guardar_cambios():
                    limpiar_pantalla()
                    print(f"El país '{Pais_Nuevo}' y sus datos fueron guardados con éxito")
                else: 
                    print("╔" + "═" * 80 + "╗")
                    print(f"║{'Se produjo un error al guardar los datos.':^79} ║")
                    print("╚" + "═" * 80 + "╝")
                break
                
            else:  
                raise Error_Repeticion("El país ya se encuentra registrado. Pruebe con otro.")
        except Error_Repeticion as e:
            limpiar_pantalla()
            print("╔" + "═" * 80 + "╗")
            print(f"║{f'ERROR:{e}':^79} ║")
            print("╚" + "═" * 80 + "╝")   
            continue
        except Exception as E:
            print(f"Ocurrió un error Inesperado: {E}")
            continue

"""
Funcion validar_continente, no recibe parametro
Solicita al usuario que ingrese un continente y valida que sea correcto.
"""
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
            print(f"║{'Recuerde respetar tildes y mayúsculas (Ej: América, África, Asia).':^79} ║")
            print("╚" + "═" * 80 + "╝")   
            continue

"""
Funcion validar_existencia, recibe como parametro un pais y una lista
Verifica si el pais ya existe en la lista.
"""
def validar_existencia(Pais,paises_lista):
    for pais in paises_lista:
        if pais["nombre"]==Pais:
            return True 
    return False

"""
Funcion listar_pais, recibe como parametro una lista
Imprime la lista en pantalla con un formato determinado.
"""
def listar_pais(lista=None):
    if lista is None:
        lista = paises_lista
        
    print("╔"+"═" *16+"╦"+"═" *18+"╦"+"═" *17+"╦"+"═" *16+"╗")
    print(f"║{' País ':^16}║{'población':^18}║{'superficie':^17}║{'continente':^16}║")

    if len(lista) == 0:
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")
        print(f"║{'No hay paises cargados':^70}║") 
        print("╠"+"═" *70+"╣")

    else:
        print("╠"+"═" *16+"╬"+"═" *18+"╬"+"═" *17+"╬"+"═" *16+"╣")
        for i in range(len(lista)):
            print(f"║{lista[i]['nombre'][:15].title():^16}║{lista[i]['población']:^18}║{lista[i]['superficie']:^17}║{lista[i]['continente'][:15].title():^16}║") 
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")

    print(f"║{'Oprima ENTER para continuar':^70}║")
    print("╚"+"═"*70+"╝")
    input("")
    limpiar_pantalla()


"""
Funcion buscar_pais, no recibe parametro
Solicita al usuario que ingrese un nombre y busca los paises que coincidan con el nombre ingresado.
"""
def buscar_pais():
    busqueda=[]
    
    seek=validar_nombre("¿Que país estas buscando?: ")
    limpiar_pantalla()

    for pais in paises_lista:
            nombre_pais = pais["nombre"].title()

            if nombre_pais.startswith(seek):
                busqueda.append([pais["nombre"],pais["población"],pais["superficie"],pais["continente"]])


    print("╔"+"═" *16+"╦"+"═" *18+"╦"+"═" *17+"╦"+"═" *16+"╗")
    print(f"║{' Pais ':^16}║{'Poblacion':^18}║{'superficie':^17}║{'continente':^16}║")

    if len(busqueda) == 0:
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")
        print(f"║{'No se encotraron paises con ese nombre':^70}║")
        print("╠"+"═" *70+"╣")

    else:
        print("╠"+"═" *16+"╬"+"═" *18+"╬"+"═" *17+"╬"+"═" *16+"╣")
        for i in range(len(busqueda)):
            print(f"║{busqueda[i][0][:15].title():^16}║{busqueda[i][1]:^18}║{busqueda[i][2]:^17}║{busqueda[i][3].title():^16}║")
        print("╠"+"═" *16+"╩"+"═" *18+"╩"+"═" *17+"╩"+"═" *16+"╣")

        
    print(f"║{"Oprima ENTER para continuar":^70}║")
    print("╚"+"═"*70+"╝")
    confirm=input("")
    limpiar_pantalla()
    confirm=""

"""
Funcion validar_opcion, recibe como parametro una lista y un mensaje
En esta funcion se valida que los valores ingresados por el usuario sean correctos y se encuentren dentro del rango permitido.
"""

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
    

"""
Funcion seleccion_criterio_ordenamiento, no recibe parametro
Solicita al usuario que ingrese un criterio de ordenamiento y retorna el valor correspondiente.
"""
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


"""
Funcion elección_orden, no recibe parametro
Solicita al usuario que ingrese una opcion de orden, valida la opcion y retorna el valor correspondiente.
"""
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
                Ascendente= False
                return Ascendente
            case "2":
                Descendente=True
                return Descendente

"""
Funcion ordenamiento, no recibe parametro
Selecciona el criterio de ordenamiento y el orden de la lista.
"""
def ordenamiento():
    global paises_lista
    Criterio=seleccion_criterio_ordenamiento()
    Orden=elección_orden()
    lista_Ordenada=sorted(paises_lista, key=lambda x: x[Criterio], reverse=Orden)
    mostrar_lista_ordenada(lista_Ordenada,Criterio,Orden)

"""
Funcion mostrar_lista_ordenada, recibe como parametro una lista y el criterio de ordenamiento.
Muestra la lista en pantalla
"""
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
     print(f"║{pais['nombre'][:15].title():^15} ║ {pais['población']:^15} ║ {pais['superficie']:^15} ║ {pais['continente'].title():^15} ║")   
    print("╠"+"═" *16+"╩"+"═" *17+"╩"+"═" *17+"╩"+"═" *17+"╣")
    print(f"║{'Presione ENTER para continuar':^69} ║")
    print("╚" + "═" * 70 + "╝")
    confirm=input("")
    limpiar_pantalla()

"""
Funcion filtro_paises, no recibe parametro
Solicita al usuario que ingrese una opcion de filtrado y llama a la funcion correspondiente.
"""
def filtrar_paises():
    limpiar_pantalla()
    print("╔" + "═" * 70 + "╗")
    print(f"║{'FILTRADO DE PAÍSES':^69} ║")
    print("╠" + "═" * 70 + "╣")
    print(f"║{'[1]-POR CONTINENTE':^69} ║")
    print(f"║{'[2]-POR RANGO DE POBLACIÓN':^69} ║")
    print(f"║{'[3]-POR RANGO DE SUPERFICIE':^69} ║")
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


"""
Funcion filtro_continentes, no recibe parametro
Solicita al usuario que ingrese un continente y filtra los paises que se encuentran en ese continente.
"""
def filtro_continentes():
    filtrados=[]
    limpiar_pantalla()
    continente=validar_continente("Continente por el cual desea filtrar: ")
    for dato in paises_lista:
        if dato['continente']==continente:
            filtrados.append(dato)
    listar_pais(filtrados)


"""
Funcion validar_rango, recibe como parametro un mensaje para pedir el valor, la clave del diccionario y el tipo de dato
En esta funcion se valida que los valores ingresados por el usuario sean correctos y se encuentren dentro del rango permitido.
"""
def validar_rango(mensaje_1,clave,conjunto_numerico):
   
    while True:
        valor_minimo=validar_numero(mensaje_1,clave,conjunto_numerico)
        try:
            valor_maximo=validar_numero("Ingrese el valor máximo: ",clave,conjunto_numerico)
            if valor_maximo>=valor_minimo:
                return valor_minimo,valor_maximo
            else:
                raise Rango_Error("El valor máximo no puede ser menor al valor mínimo")
        except Rango_Error as e:
            limpiar_pantalla()
            print("╔" + "═" * 80 + "╗")
            print(f"║{f'ERROR: {e}':^79} ║")
            print("╚" + "═" * 80 + "╝")





"""
Funcion filtro_rango, recibe como parametro un mensaje para pedir el valor, la clave del diccionario y el tipo de dato
Recorre la lista de paises y filtra los que se encuentran dentro del rango de valores dados por el usuario
"""

def filtro_rango(mensaje_1,clave,conjunto_numerico):
    filtrados_rango=[]
    minimo,maximo=validar_rango(mensaje_1,clave,conjunto_numerico)
    for pais in paises_lista:
        if minimo<=pais[clave]<=maximo:
            filtrados_rango.append(pais)
    listar_pais(filtrados_rango)
    


"""
Funcion estadistica, no recibe parametro
recorre los diccionarios con funciones anonimas para obtener los valores de promedio, maximos y minimos
tambien cuenta con un bucle para contar la cantidad de paises por continente y mostrarlo en pantalla
se podia hacer todo en una linea pero se volvia algo complejo de entender quizas.
"""


def estadistica():
    continentes=["Europa","América","África","Asia","Oceanía","Antártida"]
    print("╔"+"═" *80+"╗")
    print(f"║{' ESTADÍSTICAS DE LOS PAÍSES (cargados)':^79} ║")
    print("╠"+"═" *80+"╣")
    
    
    
    pais_mayor = max(paises_lista, key=lambda x: x['población'])
    pais_menor = min(paises_lista, key=lambda x: x['población'])
    promedio_poblacion=sum(map(lambda x:x['población'], paises_lista))/len(paises_lista)
    promedio_superficie=sum(map(lambda x:x['superficie'], paises_lista))/len(paises_lista)

    
    texto_mayor = f"País con mayor población: {pais_mayor['nombre'][:15].title()} con {pais_mayor['población']}"
    texto_menor = f"País con menor población: {pais_menor['nombre'][:15].title()} con {pais_menor['población']}"
    texto_promedio_poblacion=f"El promedio de poblacion de todos los paises es de: {promedio_poblacion:.0f} personas"
    texto_promedio_superficie=f"El promedio de superficie de todos los paises es de: {promedio_superficie:.2f} km²"
    
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
        cantidad = len(list(filter(lambda x: x['continente'] == continente, paises_lista)))
        texto = f" La cantidad de Paises de {continente.title()} en la lista es de: {cantidad}"
        print(f"║{texto:<80}║")
        
    print("╚" + "═" * 80 + "╝")
    print("\nOprima ENTER para continuar")
    input("")