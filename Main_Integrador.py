
import csv
import os
import Funciones as fun

fun.cargar_datos()

try:
 if fun.archivo_roto:
    fun.limpiar_pantalla()
    fun.mensaje_bloqueo_de_seguridad()
    input("\nPresione ENTER para salir...")
 else:
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
                fun.ordenamiento()
            case '5':
                fun.limpiar_pantalla()
                fun.filtrar_paises()
            case '6':
                fun.limpiar_pantalla()
                fun.estadistica()
            case '7':
                break   
            case _:
                fun.limpiar_pantalla()
                print("Opción inválida.")
except KeyboardInterrupt:
    fun.limpiar_pantalla()
    print("\n╔" + "═" * 70 + "╗")
    print(f"║{' FORZANDO CIERRE DEL PROGRAMA ':^70}║")
    print(f"║{' Gracias por su tiempo, vuelva pronto. ':^70}║")
    print("╚" + "═" * 70 + "╝")