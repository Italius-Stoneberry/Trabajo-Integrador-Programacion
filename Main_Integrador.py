import csv
import os
import Funciones_ as fun
ruta_archivo="Paises_data.csv"
paises=fun.cargar_datos(ruta_archivo)

while True:

    fun.mostrar_menu()
    opcion = input('Ingrese una opción: ')

    match(opcion):
        case '1':
            paises = fun.cargar_pais(paises,ruta_archivo)
        case '2':
            fun.listar_pais(paises)
        case '3':
            fun.buscar_pais(paises)
        case '4':
            paises = fun.modificar_pais(paises)
        case '5':
            paises = fun.eliminar_pais(paises)
        case '6':
            print('Hasta luego')
            break
        case _:
            print('Opcion invalida')
