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