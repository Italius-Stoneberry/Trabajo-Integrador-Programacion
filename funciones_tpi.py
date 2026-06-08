def mostrar_menu():
    print('''\n---Menu---
1. Agregar pais
2. Listar paises
3. Buscar pais
4. Modificar pais
5. Eliminar
6. Salir''')


##hacer funciones para validar y no ser repetitivo



def agregar_pais(paises):
    while True:
        nombre = input('Ingrese el nombre del pais: ')
        if not nombre.isalpha() or len(nombre) < 2: #valida que el nombre sea solo letras y tenga al menos 2 caracteres por si es una abreviatura
            #guardar en title o en capitalize
            print('Error: El nombre debe ser una palabra de al menos 2 letras (sin números ni simbolos).')
            continue
        break

    while True:
        try:
            poblacion = int(input('Ingrese la poblacion del pais: '))
        except ValueError:
            print('Error: La poblacion debe ser un numero.')
            continue
        break
    while True:
        try:
            superficie = float(input('Ingrese la superficie del pais: '))
        except ValueError:
            print('Error: La superficie debe ser un numero.')
            continue
        break
    while True:
        continente = input('Ingrese el continente del pais: ')
        if not continente.isalpha() or len(continente) < 2: #valida que el continente sea solo letras y tenga al menos 2 por que me quedo de arriba, nose si hay abreviaturas de continentes, solo latam creo
        # aca igual
            print('Error: El continente debe ser una palabra de al menos 2 letras (sin números ni simbolos).')
            continue
        else:
            break

    pais_nvo = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente' : continente
    }

    paises.append(pais_nvo)
    print('Pais agregado correctamente.')
    return paises

def listar_paises(paises):
    if not paises:
        print('No hay paises que mostrar.')
    else:
        for pais in paises:
            print()
            for k,v in pais.items():
                print(f'{k.capitalize()}: {v.capitalize()}')#aca muestra los paises en capitalize

def buscar_pais(paises):
    if not paises:
        print('No hay paises cargados.')
    else:
        nombre_pais = input('Ingrese el pais a buscar: ')
        encontrado = False
        for pais in paises:
            if nombre_pais.lower() == pais['nombre'].lower(): #aca busca en lower por que nose como carguen los paises ni los que tenga cargados
                print(f'Pais encontrado: {pais}')
                encontrado = True
                break #sale del for al encontrarlo eso me falto decirle en la clase :(
        if not encontrado:
            print('Pais no encontrado.')

def modificar_pais(paises):
    if not paises:
        print('No hay paises cargados.')
    else:
        nombre_pais = input('Ingrese el pais a modificar: ')
        encontrado = False
        for pais in paises:
            if nombre_pais.lower() == pais['nombre'].lower(): #aca busca en lower por que nose como carguen los paises ni los que tenga cargados
                print(f'Pais encontrado: {pais}')
                encontrado = True
                break #sale del for al encontrarlo

            #aca lo mismo que arriba pero para modificar
                while True:
                    try:
                        pais['poblacion'] = int(input(f'Ingrese la nueva poblacion para {pais['nombre']}: '))
                        break
                    except ValueError:
                        print('Error: La poblacion debe ser un numero.')
                        continue
                while True:
                    try:
                        pais['superficie'] = float(input(f'Ingrese la nueva superficie para {pais['nombre']}: '))
                        break
                    except ValueError:
                        print('Error: La superficie debe ser un numero.')
                        continue
                print('Pais modificado')
                break #es para que no siga buscando mas paises con el mismo nombre por si hay varios(ojala no)

        if not encontrado:
            print('Pais no encontrado.')
        
    return paises

def eliminar_pais(paises):
    if not paises:
        print('No hay paises cargados.')
    else:
        nombre_pais = input('Ingrese el pais a eliminar: ')
        encontrado = False
        for pais in paises:
            if nombre_pais.lower() == pais['nombre'].lower():
                print(f'Pais encontrado')
                encontrado = True
                paises.remove(pais)
                print('Pais eliminado.')
                break #sale del for al borrarlo

    if not encontrado:
            print('Pais no encontrado.')
    
    return paises

import os
import sys
import time
import threading

# Habilitar códigos ANSI en Windows
if os.name == 'nt':
    os.system("")

# Evento global para controlar el hilo de forma segura
evento_detener = threading.Event()

def animar_area_superpuesta():
    ancho = 70
    
    patron_base = [
        "~~~~...~~~#####~~~...~~~~",
        "~~...::########:::..~~~~~",
        "~..:::::#####:::::..~~~~~",
        "~~..::::####::::..~~~~...",
        "~~~~...:###:...~~~~~.....",
        "~~~~~~..##..~~~~~~~~~~~.."
    ]
    patron_mapa = [linea * 3 for linea in patron_base]
    
    mascara = [
        ("      .·~", 12, "~·.      "),
        ("   /  ",    18, "  \\   "), 
        (" |  ",      22, "  | "),
        (" |  ",      22, "  | "),
        ("   \\  ",    18, "  /   "), 
        ("      '·_", 12, "_·'      ")
    ]
    
    opciones = [
        " [1] Agregar pais",
        " [2] Listar paises",
        " [3] Buscar pais",
        " [4] Ordenamiento",
        " [5] Filtros",
        " [6] Estadísticas"
    ]

    frame = 0
    
    while not evento_detener.is_set():
        # 1. MAGIA ANSI: \033[s GUARDA la posición actual del cursor (donde está el input)
        sys.stdout.write("\033[s")
        
        # 2. Mueve el cursor a la fila 1, columna 1 para redibujar el menú arriba
        sys.stdout.write("\033[1;1H")
        
        # Armamos el menú entero en un string
        buffer = ""
        buffer += "╔" + "═" * ancho + "╗\n"
        buffer += f"║{' Hola bienvenido al gestor de paises ':^70}║\n"
        buffer += "╠" + "═" * ancho + "╣\n"

        for i in range(6):
            texto_opcion = opciones[i]
            prefijo, ancho_movil, sufijo = mascara[i]
            mapa_linea = patron_mapa[i]
            
            idx = frame % 25
            porcion_movil = mapa_linea[idx : idx + ancho_movil]
            
            globo_str = f"{prefijo}{porcion_movil}{sufijo}"
            espacio_medio = ancho - len(texto_opcion) - len(globo_str)
            
            buffer += f"║{texto_opcion}{' ' * espacio_medio}{globo_str}║\n"

        buffer += "╠" + "═" * ancho + "╣\n"
        buffer += f"║{' [7] Salir':<70}║\n"
        buffer += "╚" + "═" * ancho + "╝\n"
        
        # 3. MAGIA ANSI: \033[u RESTAURA el cursor al lado de tu input
        buffer += "\033[u"
        
        # Imprimimos y forzamos la salida
        sys.stdout.write(buffer)
        sys.stdout.flush()
        
        frame += 1
        time.sleep(0.15)

def iniciar_programa():
    # Limpieza inicial única
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        # Preparamos la terminal y arrancamos la animación de fondo
        evento_detener.clear()
        sys.stdout.write("\033[1;1H") # Cursor arriba
        hilo = threading.Thread(target=animar_area_superpuesta, daemon=True)
        hilo.start()
        
        # Nos aseguramos de poner el input estático en la línea 13 (debajo del menú)
        sys.stdout.write("\033[13;1H")
        sys.stdout.write(" " * 50 + "\r") # Limpiamos la línea por si quedó texto viejo
        
        # TU INPUT NORMAL. El programa frena acá, pero el menú sigue moviéndose arriba.
        opcion = input("Seleccione una opción: ")
        
        # Detenemos la animación y esperamos que el hilo cierre limpio
        evento_detener.set()
        hilo.join()
        
        # Lógica de tu programa
        if opcion == '7':
            print("\nSaliendo...")
            break
        elif opcion in ['1', '2', '3', '4', '5', '6']:
            # Limpiamos la pantalla para mostrar la acción seleccionada
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Elegiste la opción {opcion}. Ejecutando lógica...\n")
            
            # Simulamos que tu programa hace algo y luego vuelve al menú
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            sys.stdout.write("\033[14;1HOpción inválida. ")
            time.sleep(1)

if __name__ == "__main__":
    iniciar_programa()