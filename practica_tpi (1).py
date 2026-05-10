from funciones_tpi import mostrar_menu
from funciones_tpi import agregar_pais
from funciones_tpi import listar_paises
from funciones_tpi import buscar_pais
from funciones_tpi import modificar_pais
from funciones_tpi import eliminar_pais

# Simulacion de datos
paises = [
    {"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400, "continente": "America"},
    {"nombre": "Japon", "poblacion": 125800000, "superficie": 377975, "continente": "Asia"}
]

while True:

    mostrar_menu()
    opcion = input('Ingrese una opción: ')

    match(opcion):
        case '1':
            paises = agregar_pais(paises)
        case '2':
            listar_paises(paises)
        case '3':
            buscar_pais(paises)
        case '4':
            paises = modificar_pais(paises)
        case '5':
            paises = eliminar_pais(paises)
        case '6':
            print('Hasta luego')
            break
        case _:
            print('Opcion invalida')