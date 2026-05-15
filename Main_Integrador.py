
import csv
import os
import Funciones_de_prueba as fun
ruta_archivo="Paises_data.csv"
paises=fun.cargar_datos(ruta_archivo)

#se borro el código que estaba en el main para pasar a un formato de main más ordenado y legible

while True:
    fun.mostrar_menu()
    opcion = input("Elija una opción: ")

    
    match(opcion):
        case '1':
            paises = fun.agregar_paises()
        case '2':
            fun.listar_pais()            
        case '3':
            fun.buscar_pais()
        case '4':
            fun.eliminar_pais()
        case '5':
            fun.modificar_pais()  
        case '6':
            break
        case _:
            print("Opción inválida.")
