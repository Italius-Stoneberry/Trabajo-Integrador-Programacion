
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
            # #paises = fun.agregar_paises() /ya no hace falta que esté igualada a la fación por que todo ocurre en el módulo de funciones            fun.agregar_paises()
       
            fun.agregar_paises()
        case '2':
            fun.listar_pais()            
        case '3':
            fun.buscar_pais()
        case '4':
            fun.eliminar_pais()
        case '5':
            fun.modificar_pais() 
        case '7':
            fun.ordenamiento() #BROO esta opción tenes que agregarla al menú
        case '6':
            break
        case _:
            print("Opción inválida.")
