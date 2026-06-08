
import csv
import os
import Funciones_de_prueba as fun
#ruta_archivo="Paises_data.csv"<-BROOO: lo saco porque declare la ruta completa en el módulo de funciones
#paises=fun.cargar_datos()#BROO por eso acá le saqué el parámtero y tambien la llamo sin igualar a nada
fun.cargar_datos()

#se borro el código que estaba en el main para pasar a un formato de main más ordenado y legible

while True:
    fun.mostrar_menu()
    opcion = input("Elija una opción: ")

    
    match(opcion):
        case '1':
            fun.limpiar_pantalla()
            fun.agregar_paises()
            
        case '2':
            fun.limpiar_pantalla()
            fun.listar_pais()            
        case '3':
            fun.limpiar_pantalla()
            fun.buscar_pais()
        case '4':
            fun.limpiar_pantalla()
            fun.ordenamiento() #BROO esta opción tenes que agregarla al menú
        case '5':
            fun.limpiar_pantalla()
            fun.filtrar_paises()#BROO esta opción tambien hay que agregarla al menú
        case '6':
            fun.limpiar_pantalla()
            fun.estadistica()
        case '7':
            break   
        case _:
            fun.limpiar_pantalla()
            print("Opción inválida.")