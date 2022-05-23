# Creamos una funcion que permite definir un bloque de código reutilizable que se puede ejecutar muchas veces dentro de tu programa.
def robot():

    # El robot completa el objetivo si todos los lotes estan regados
    estadoObjetivo = {'A': '0', 'B':  '0', 'C': '0'}
    # Inicializmos una variable para el costo.
    costo = 0
    # Mostramos por pantalla que opciones va a tener el usuario
    print('''   Estimado usuario recuerde que las ubicaciones están dadas de la siguinte manera
  [Lote_1 = A]
  [Lote_2 = B]
  [Lote_3 = c] '''
          )
    # Se muestra por pantallo los lotes disponibles y un mensaje para elegir que opciones quiere.
    print('''Esimado usuario digite la ubicacion donde se encunetra el robot 
  [Lote_1]
  [ Lote_2]
  [Lote_3]''')
    ubicacionLote = input(
        "Digite donde se encuentra el robot:  ")  # Le pedimos al usuario que digite donde se encuentra el robot, este dato es de tipo string
    # '''
    # Para la primera sentencia if, se lee que si el usuario digita la opciones A el robot se encuentra en el lote 1
    # '''
    #Si la ubicacionLote es = A entonces dira que el robot se encuentra la opcion A
    if ubicacionLote == 'A':
        print("El robot se encunetra en la ubicación:  A")
        #Usuario ingresa el estado del lote y muestra la ubicacion del lote que se escogio
        estadoDelLoteA = input("Digite el estado del lote:   " +    ubicacionLote)
        #usuario digita el estado del lote B
        estadoLoteB = input("Digite el estado del lote B:    "  )
        #Usuaio digita el estado del lote C
        estadoLoteC = input("Digite el estado del lote  C:    " )
        if estadoDelLoteA == '1':#Si la opcion es 1, imprimira que el lote esta seco
            print("Ubicacion: " + ubicacionLote + '   esta seco')
            estadoObjetivo['A'] = '0' #Como va a regar, cambia de estado a 0 que es 
            print("*****Regando el lote************") #Informa que el lote está siendo regado
            print("Lote " + ubicacionLote + ' totalemente regado') #Informa que el riego ya finalizo
            costo += 1  # Aumenta el costo
            print("Valor del costo  =  " + str(costo)) #Aqui solo se muestra el valor del costo
            if estadoLoteB == '1':#Si estado del lote B es igual a 1 
                print("El lote B :    " + estadoLoteB + "   esta seco")#muestra un mensaje donde el lote B esta seco
                print("-------Moviendose a la ubicación    " +
                  "  B " + "-------------")  #Simula que esta moviednose a la ubicacion B
                print("********Regando el lote************") #Simula que se riega el lote
                costo += 1  # aumento del costo del riego
                print("El valor actual es:  " + str(costo)) #Muestra el valor del costo
                print("Lote B totalemente regado") #Informa que el lote ya está regado
                # '''
                # Aplicamos la misma logica para el lote C
                # '''
                if estadoLoteC == '1':
                    print("El lote:     " + estadoLoteC + "esta seco")
                    print("-------Moviendose a la ubicación    " +
                      "C" + "-------------")
                    costo += 1  # aumento del costo del riego
                    print("El valor actual es:  " + str(costo))
                    print("Lote C totalemente regado")
                    # '''
                    # Le decimos al usuario que todos los lotes estan regados
                    # por ende no hay que hacer, 
                    # '''
                else:
                    print("**********Ninguna accion que realizar**********")
                    print("El valor del costo actual es:  " + str(costo))
