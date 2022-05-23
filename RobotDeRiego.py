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
    # Si la ubicacionLote es = A entonces dira que el robot se encuentra la opcion A
    if ubicacionLote == 'A':
        print("El robot se encunetra en la ubicación:  A")
        # Usuario ingresa el estado del lote y muestra la ubicacion del lote que se escogio
        estadoDelLoteA = input("Digite el estado del lote:   " + ubicacionLote)
        # usuario digita el estado del lote B
        estadoLoteB = input("Digite el estado del lote B:    ")
        # Usuaio digita el estado del lote C
        estadoLoteC = input("Digite el estado del lote  C:    ")
        if estadoDelLoteA == '1':  # Si la opcion es 1, imprimira que el lote esta seco
            print("Ubicacion: " + ubicacionLote + '   esta seco')
            # Como va a regar, cambia de estado a 0 que es
            estadoObjetivo['A'] = '0'
            # Informa que el lote está siendo regado
            print("*****Regando el lote************")
            # Informa que el riego ya finalizo
            print("Lote " + ubicacionLote + ' totalemente regado')
            costo += 1  # Aumenta el costo
            # Aqui solo se muestra el valor del costo
            print("Valor del costo  =  " + str(costo))
            if estadoLoteB == '1':  # Si estado del lote B es igual a 1
                # muestra un mensaje donde el lote B esta seco
                print("El lote B :    " + estadoLoteB + "   esta seco")
                print("-------Moviendose a la ubicación    " +
                      "  B " + "-------------")  # Simula que esta moviednose a la ubicacion B
                # Simula que se riega el lote
                print("********Regando el lote************")
                costo += 1  # aumento del costo del riego
                # Muestra el valor del costo
                print("El valor actual es:  " + str(costo))
                # Informa que el lote ya está regado
                print("Lote B totalemente regado")
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

        if estadoDelLoteA == '0':  # Si estado del lote es 0=regado
            # Le dice al usuario que ya regado
            print("***El lote A ya está regado: ESTADO = 0")
            if estadoLoteB == '1':  # Si el estado del lote B es 1 siginifica que esta seco
                # Muestra que esta seco
                print("-----Ubicacion B esta seco--------")
                print("")
                print("")
                print("")
                # Simula que riega el lote B
                print("*****Regando el lote B*******")
                costo += 1  # incrementa el costo al ir a regar
                print("El valor del costo actual es:    " + str(costo))
               # Despues de regar cambia de estado
                estadoObjetivo['B'] = '0'  # Cambia de estado a regado
                costo += 1
                print("|------------------------------------|")
                print("| -------- Lote B regado-------------|")
                print("|------------------------------------|")
                print("|------------------------------------|")
                # Actualizamos el valor del costo
                print("Costo actualizado:   " + str(costo))
                print("")
                print("")
                print("")
                if estadoLoteC == '1':
                    # Si estado del lote C es igual a 1
                    # imrprime que el lote esta seco
                    print("-----Ubicacion C esta seco--------")
                    print("*** Regando el lote********")
                    costo += 1  # incrementa el costo al ir a regar
                    print("El valor del costo actual es:    " +
                          str(costo))  # imprimimos el costo
                    # Despues de regar cambia de estado
                    estadoObjetivo['C'] = '0'
                    costo += 1  # variable die que el costo aumentará
                    print("|------------------------------------|")
                    # Muestra un mensaje diciendo que el lote ya ha sido regado
                    print("| -------- Lote C regado ------------|")
                    print("|------------------------------------|")
                    print("|------------------------------------|")
                    print("Costo actualizado:   " + str(costo))
            else:  # Caso contrario si el usuario dijita si el lote B y C estan regados
                # como todos estan regados no hay nada que hacer
                print("Ninguna accion que realizar" + str(costo))
                # imprimimos el valor del costo
                print("El valor del costo es:   " + str(costo))
                # Muestra el mensaje que ya estan regados
                print("Ubicacion B y C ya están regadas.")
    #Programacion para el lote B
    #Un elif para controlar bloques de codigo 
    elif ubicacionLote == 'B':  #Si el usuario digita B
        #Muestra por consolo donde se encuentra el robot
        print("El robot se encunetra en la ubicación:  B") #
        estadoDelLoteB = input("Digite el estado del lote:   "  + ubicacionLote) #Pedimos al usuario si el lote esta seco o regado
        estadoLoteA = input("Digite el estado del lote A:    ") #Digita el estado del lote A
        estadoLoteC = input("Digite el estado del lote C:    ") #Digita el estado del lote B
        print("El valor del costo es actual es:   " + str(costo)) #El valor del costo actual es
        if estadoDelLoteB == '1': #Si el estado del lote es igual a 1 siginifica que esta seco
          print("*******Regando el lote************") #Simula que el loto esta siendo regado
          #El estado del lote cambia a B 
          estadoObjetivo['B'] = '0'
          print("Lote " +   ubicacionLote  + ' tatalmente regado') #Le dice al usuario que ya acabo 
          costo += 1 #Aumenta el costo
          print("Valor del costo  =  "    + str(costo)) # Concatenar el valor del costo con su costo, str para cambiar a tipo string 
          #Generamos linea de código para el lote A.
          if estadoLoteA == '1':#PARA EL LOTE A
              print("El lote :   " +   'A'    +    "   ESTA SECO")
              print("*****Regando el lote A ********* ") #Simula que essta siendo regado
              costo += 1 #aumento del costo del riego
              print("El valor actual es:  "   +   str(costo)) #El valor ahora se actualiza
              print("Lote A totalemente regado") #El robot acaba de limpiar el lote A

              #PARA EL LOTE C
              if estadoLoteC == '1': #SI EL LOTE C = 1
                  print("El lote:     " + "C" +     " esta seco") # DICE QUE EL LOTE ESTA SECO
                  print("*****Regando el lote   C") #Simula que ya ha regado el lote
                  costo += 1 #aumento del costo del riego
                  print("El valor actual es:  "   +   str(costo))   #El valor actual del lote
                  print("Lote C totalemente regado") # Le dice al usuario que ya terminó 
          else:
              print("Lote A ya está regado") #Muestra que el lote A ya esta regado
              print("Lote C ya esta regado") #Muestra que el lote C ya esta regado 
        if estadoDelLoteB == '0':  #Si estado del lote B = 0 entonces
            print("El lote B ya esta regado")  #El lote B esta regado, no hay cambios
            if estadoLoteA == '1': #Si estado del lota es 1
                print("****Lote A seco*******") #El lote esta seco
                print("")#Salto de linea
                print("")
                print("")
                print("*****Regando lote A") #Simula que esta regando el lote A
                costo +=1 #incrementa el costo al ir a regar
                print("El valor del costo actual es:    "+  str(costo)) #Actualiza el valor del costo
                #Despues de regar cambia de estado
                estadoObjetivo['A'] = '0' #El estado del lote A cambia a regado
                costo += 1 #por ende aumentará el costo
                print("|------------------------------------|") 
                print("| **********Lote A regado************|")  #Le dice al usuario que ya acabó de regar
                print("|------------------------------------|")
                print("|------------------------------------|")
                print("Costo actualizado:   " + str(costo)) #Costo actualizado
                print("")
                print("")
                print("")
                if estadoLoteC == '1':
                    print("****LOTE C ESTA SECO")
                    costo +=1 #incrementa el costo al ir a regar
                    print("El valor del costo actual es:    "+  str(costo))
                    #Despues de regar cambia de estado
                    estadoObjetivo['C'] = '0'
                    costo += 1
                    print("|------------------------------------|") 
                    print("| ***********LOTE C REGADO***********|") 
                    print("|------------------------------------|")
                    print("|------------------------------------|")
                    print("Costo actualizado:   " + str(costo))
            else:

                print("Lote A ya está regado")
                print("Lote C ya esta regado") 


    elif ubicacionLote == 'C':

        print("---- Estimado usuario el robot se encuentra en la ubicacion C  ---")
        estadoDelLoteC = input("Digite el estado del lote:   "  + ubicacionLote)
        estadoLoteA = input("Digite el estado del lote A:    ")
        estadoLoteB = input("Digite el estado del lote C:    ")
        print("El valor del costo es actual es:   " + str(costo))            





