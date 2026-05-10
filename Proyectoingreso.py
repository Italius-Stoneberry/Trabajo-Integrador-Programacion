##devido a la cantidad de tiempo que nos dieron me tome la libertad de investigar un poco con las interfaces, ultimamente estuve configurando un
#servidor nas y otras cosas y vi que usaban un monton este tipo de interfaz y me gustaron, despues investigando tambien aprendi que no requieren
#librerias ni framewors etc, asique las implemente
ancho=70 #primero las queria implementar con variables pero dps tuve que diseñar medios bloques y ya no tenia mucho sentido seguir declarando


#Con respecto al diseño del ejercicio me parecio raro pero entendible, tener que hacer el ejercicio con listas paralelas.
# debido a que es mas simple de trabajar que una matriz anidada pero a la vez tiene mas limitaciones (no poder shortear los titulos por ejemplo debido a la perdida del orden en los indices)
# pero entendible por un enfoque de una dificultad media baja,
# simplemente me parecio curioso la decision y quise hacer la aclaracion. 

titulos=[] #variable de titulos, se guardan los titulos de los libros
ejemplares=[]  # se guardan la cantidad de copias de los libros, la unica limitacion o diferencia respecto a la demostracion es que no podes agregar titulos con ejemplares nulos
                    #no lo vi logico permitir tal cosa,
prestamos=[]   #Esta lista extra es para registrar los prestamos, que hace? bueno surgio de el problema del prestamo fantasma, 
                    # mientras trabajaba surgio la duda, y si el usuario intenta devolver libros que nunca pidio? lo va a poder hacer y el programa
                    # lo va a permitir perfectamente, y como solucionarlo? Bueno cuando se crean los libros esa lista se inicializa en 0 y cuando pedis un libro
                    # aumenta en 1 y el stock disminuye, y cuando devolves es viseversa.
                    # Esto es elemental para no perder el valor original del stock 
busqueda=[[],[]]    #Al incorporar un sistema de busqueda relativamente inteligente, necesitaba una lista para guardar los resultados y los indices
resultado=""
seek=""             #

contador=0          #variable que uso con multiples propositos relacionados a las validaciones
confirm=""







#while iterador del menu
while True:

    ##constructor de menu
    
    print("╔"+"═" *ancho+"╗")
    print(f"║{' Hola bienvenido a tu administrador de biblioteca ':^70}║")
    print("╠"+"═" *ancho+"╣")
    print(f"║{' [1] Ingresar Títulos':<70}║")
    print(f"║{' [2] Ver Catálogo':<70}║")
    print(f"║{' [3] Consultar Disponibilidad':<70}║")
    print(f"║{' [4] Listar Agotados':<70}║")
    print(f"║{' [5] Agregar Nuevos Títulos':<70}║")
    print(f"║{' [6] Actualizar Ejemplares (Préstamo/Devolución)':<70}║")
    print("╠"+"═" * ancho + "╣")
    print(f"║{' [7] Salir':<70}║")
    print("╚"+"═" * ancho + "╝")
    opcion = input(" Seleccione una opción: ")

    if opcion =="1":
        
        ##if len(titulos)==0:

            while contador<=0:
                print("╔"+"═"*70+"╗")
                contador=int(input("Cuantos libros desea agregar?\n"))
            print("Exelente comencemos!!")
            for i in range(contador):
                print("═"*70)
                titulos.append(input("Que titulo desea ingresar ?\n").lower())
                confirm=(input("Cuantos ejemplares desea ingresar?\n"))
                #validador de numeros (su funcion es no permitir ingresar libros con valores nulos ni palabras o otros datos, solo numeros positivos)
                while not confirm.isdecimal() or int(confirm) <= 0:
                    confirm=input("Lo siento ese valor no es valido, ingrese un valor nuevamente\n")
                #cuando es valor es correcto ingresa aca, construi multiples validadores del mismo tipo a lo largo del examen
                #practicamente las variables confirm y contador se reinician casi en cada funcion del programa.
                ejemplares.append(int(confirm))
                prestamos.append(0)
                print(f"El libro {titulos[-1].title()} con {ejemplares[-1]} Ejemplares\nSe ingreso correctamente")
                confirm=""    
        #print(f"{titulos}{ejemplares}") control
        
    """
        Esto quedo comentado debido a una mala interpretacion de los titulos, ya que entendi que el punto 1 era solo para una carga inicial
        de contenido y luego todo se debia realizar desde la accion 5 (incorporar nuevos titulos), pero explicaciones posteriores en clase,
        hicieron que comente la funcionalidad.


        else:
            print('Lo sentimos la biblioteca ya cuenta con libros!\nSi desea agregar mas debe seleccionar "[5] Agregar Nuevos libros"')
        #Pantalla de confirmacion para que el usuario pueda ver la info solicitada antes de salir al menu   
        print("╠"+"═"*70+"╣")
        confirm=input(f"{"Oprima cualquier tecla para continuar":^70}\n")
        confirm=""

    """
    
    if opcion =="2":
        ##-----------interfaz------------
        print("╔"+"═" *55+"╦"+"═" *14+"╗")
        print(f"║{' Titulos ':^55}║{'Ejemplares':^14}║")
        print("╠"+"═" *55+"╬"+"═" *14+"╣")
        

        for i in range(len(titulos)):
            print(f"║{titulos[i].title():^55}║{ejemplares[i]:^14}║")
        
        print("╠"+"═" *55+"╩"+"═" *14+"╣")
        print(f"║{"Oprima ENTER para continuar":^70}║")
        #Pantalla de confirmacion para que el usuario pueda ver la info solicitada antes de salir al menu  
        print("╚"+"═"*70+"╝")
        confirm=input("")
        confirm=""
        
        
        
        
        """
        Primera version
        print("╠"+"═"*70+"╣")
        confirm=input(f"{"Oprima cualquier tecla para continuar":^70}\n")
        confirm=""
        """
    
    if opcion =="3":
        busqueda=[[],[]]

        while confirm=="":
            indice=0
            seek=input("Que libro estas buscando?\n").lower()

            for titulo in titulos:
                
                if len(seek) > len(titulo):#Descartamos los libros con menos palabras
                    indice+=1
                    continue

                iguales=True

                for i in range(len(seek)):
                    letra_titulo=titulo[i]
                    letra_seek=seek[i]
                    if letra_seek != letra_titulo:
                        iguales=False
                        confirm=""
                        break
                    if iguales == True:
                        resultado=titulo
                        confirm="1"
                if confirm == "1":    
                    busqueda[0].append(resultado)
                    busqueda[1].append(ejemplares[indice])
                    confirm=""

                indice+=1
            """Logicamente creo que fue lo mas dificil, el reto autoimpuesto, esto lo que hace es validar letra por letra, si la palabra buscada tiene unos cuantos aciertos entonces
            se va a guardar en la lista "busqueda" con el respectivo indice del libro, por que con el indice ? para poder pedirle a la tabla cuantos libros tengo en stock
            lo que fue un poco mas dificil de hacer con listas paralelas,
            La idea era que si tenes 4 libros de harry potter , como puede ser HP y la piedra filosofal, HP y el caliz de fuego, HP ....
            al introducir las palabras como harry, harry potter, har, te arroje estas opciones en orden en el que fueron introducidas, y que el usuario pueda decidir
            si es o no el libro que estaba buscando"""
            

            print("╔"+"═" *55+"╦"+"═" *14+"╗")
            print(f"║{' Titulos ':^55}║{'Ejemplares':^14}║")
            print("╠"+"═" *55+"╬"+"═" *14+"╣")
            for i in range(len(busqueda[0])):
                    print(f"║{busqueda[0][i].title():^55}║{busqueda[1][i]:^14}║")
                    
            if len(busqueda[0]) == 0:
                print(f"║{"No se encotraron Libros con ese titulo":^55}║{"0":^14}║")
            
            print("╠"+"═" *55+"╩"+"═" *14+"╣")
            print(f"║{"Oprima ENTER para continuar":^70}║")
            print("╚"+"═"*70+"╝")
            confirm=input("")
            confirm=""
            break

            """
            Esta es una version anterior que fui modificando con el paso de los dias pero la logica se complico demaciado, habian varias lineas de validadores que hacian lo mismo
            pero es media confusa, ya que originalemnte la pense para que el programa te pregunte por cada titulo que encontro, pero pense que seria un
            mejor diseño directamente que te muestre un cuadro siguiendo la linea del diseño del menu, y mucho mas intuitivo para el usuario, con menos texto que leer

            
            if len(busqueda[0])>=1:



                for i in range(len(busqueda[0])):
                    print(f"Usted estaba buscando el titulo {busqueda[0][i].title()} ?")
                
                    while confirm != "n" and confirm != "y":
                        confirm=input("Oprima Y/N\n").lower()
                    

                    if confirm =="y":
                        print(f"El titulo {busqueda[0][i].title()} tiene {busqueda[1][i]} copias")
                        confirm=""
                        resultado=""
                        
                        break
                    else:
                        confirm=""
                        resultado="nf"
                          
            
            if len(busqueda[0])==0 or resultado=="nf":
                print("Lo sentimos, Titulo no encontrado\nDesea dejar de buscar?")
                
                while confirm != "n" and confirm != "y":
                    confirm=input("Oprima Y/N\n").lower()

                if confirm == "y":
                    confirm=""
                    resultado=""
                    
                    break

                elif confirm == "n":
                    resultado=""
                    confirm=""

            elif resultado !="nf":
            #Pantalla de confirmacion para que el usuario pueda ver la info solicitada antes de salir al menu   
                print("╠"+"═"*70+"╣")
                confirm=input(f"{"Oprima cualquier tecla para continuar":^70}\n")
                confirm=""
                resultado=""
                break   

                """
        

        


    if opcion =="4":

        contador=0
        print("╔"+"═" *70+"╗")
        print(f"║{' Titulos Agotados':^70}║")
        print("╠"+"═" *70+"╣")
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                print(f"║{titulos[i]:^70}║")
                contador+=1
        if contador == 0:
            print(f"║{"No se encotraron titulos Sin Ejemplares":^70}║")
        print("╠"+"═" *70+"╣")
        print(f"║{"Oprima ENTER para continuar":^70}║")
        #Pantalla de confirmacion para que el usuario pueda ver la info solicitada antes de salir al menu  
        print("╚"+"═"*70+"╝")
        confirm=input("")
        confirm=""
        
    if opcion =="5":
        if len(titulos)>=1:

            while confirm=="":
                confirm=(input("Que titulo desea Agregar ?\n").lower())
                for titulo in titulos:
                    if confirm==titulo:
                        print(f"{"Lo sentimos ese titulo ya esta en Existencia":^70}")
                        confirm=""

            titulos.append(confirm)
            confirm=""
        
            confirm=(input("Cuantos ejemplares desea ingresar?\n"))
            while not confirm.isdecimal() or int(confirm) <= 0:
                confirm=input("Lo siento ese valor no es valido, ingrese un valor nuevamente\n")
            ejemplares.append(int(confirm))
            prestamos.append(0)

            print(f"El libro {titulos[-1].title()} con {ejemplares[-1]} Ejemplares\nSe ingreso correctamente")
            confirm=""    
            #print(f"{titulos}{ejemplares}") control   
            print("╔"+"═" *ancho+"╗")
            print(f"║{"Oprima ENTER para continuar":^70}║")  
            print("╚"+"═"*ancho+"╝")
            confirm=input("")
            confirm=""
        else: ##Este apartado lo ingrese por si querias agregar un titulo sin antes hacer el ingreso del 1, como escribi un poco mas arriba
            #inicialmente interprete que los libros si o si debian acceder primero por el punto 1 y luego por el punto 5, esta parte del codigo quedo(todavia es funcional igualmente)
            print("Lo siento, Debe ingresar titulos primero (opcion [1])!")
            print("╔"+"═" *ancho+"╗")
            print(f"║{"Oprima ENTER para continuar":^70}║")  
            print("╚"+"═"*ancho+"╝")
            confirm=input("")
            confirm=""
        



    if opcion =="6":
        contador=""
        
        if len(titulos)>=1:
        
            confirm="-1"
            while int(confirm)<0 or int(confirm)>len(titulos)+1:

                print("╔"+"═" *55+"╦"+"═" *14+"╗")
                print(f"║{' Titulos ':^55}║{'Ejemplares':^14}║")
                print("╠"+"═" *55+"╬"+"═" *14+"╣")
                for i in range(len(titulos)):
                    print(f"║[{i+1}]{titulos[i]:^52}║{ejemplares[i]:^14}║")
                print("╠"+"═" * ancho + "╣")
                print(f"║{f'[{len(titulos)+1}] Salir':<70}║")
                print("╚"+"═" * ancho + "╝")


                confirm=input(f"{"Seleccione un titulo a Actualizar [valor]":^70}\n")

                if not confirm.isdigit() or (int(confirm)<0 or int(confirm)>len(titulos)+1):
                    print(f"{"Valor erroneo":^70}")
                    confirm="-1"
            
            if int(confirm) == len(titulos)+1:
                contador=0
                continue

            contador=(input(f"Desea Pedir Prestado [1] o Devolver [2] un ejemplar de {titulos[int(confirm)-1]} "))
        
            while contador!="1" and contador!="2":
                contador=input(f"{"Seleccione [1] para pedir o [2] para devolver":^70}\n")
                if not contador.isdigit():
                    print(f"{"Valor erroneo":^70}")

            if int(contador) == 1 and ejemplares[int(confirm)-1]>=1:
                ejemplares[int(confirm)-1]-=1
                prestamos[int(confirm)-1]+=1
                print("Se Registro el prestamo con Exito!")
            
            elif int(contador) == 2 and prestamos[int(confirm)-1]>=1:
                ejemplares[int(confirm)-1]+=1
                prestamos[int(confirm)-1]-=1
                print("Se Registro la devolucion con Exito!")
            else:
                print("Lo siento, no se pudo autorizar la solicitud")
                contador=0
        
        else:
            print("Lo siento no tiene titulos disponibles!")
        
        print("╔"+"═" *ancho+"╗")
        print(f"║{"Oprima ENTER para continuar":^70}║")  
        print("╚"+"═"*ancho+"╝")
        confirm=input("")
        confirm=""
        contador=0


    if opcion =="7":
        break
    else:
        continue