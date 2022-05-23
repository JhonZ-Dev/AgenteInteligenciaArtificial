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
    if ubicacionLote == 'A':
        print("El robot se encunetra en la ubicación:  A")
        estadoDelLoteA = input("Digite el estado del lote:   " +    ubicacionLote)
        estadoLoteB = input("Digite el estado del lote B:    "  )
        estadoLoteC = input("Digite el estado del lote  C:    " )
        if estadoDelLoteA == '1':
            print("Ubicacion: " + ubicacionLote + '   esta seco')
            estadoObjetivo['A'] = '0'
            print("*****Regando el lote************")
            print("Lote " + ubicacionLote + ' totalemente regado')
            costo += 1  # Aumenta el costo
            print("Valor del costo  =  " + str(costo))
            if estadoLoteB == '1':
                print("El lote B :    " + estadoLoteB + "   esta seco")
                print("-------Moviendose a la ubicación    " +
                  "  B " + "-------------")
                print("********Regando el lote************")
                costo += 1  # aumento del costo del riego
                print("El valor actual es:  " + str(costo))
                print("Lote B totalemente regado")
                if estadoLoteC == '1':
                    print("El lote:     " + estadoLoteC + "esta seco")
                    print("-------Moviendose a la ubicación    " +
                      "C" + "-------------")
                    costo += 1  # aumento del costo del riego
                    print("El valor actual es:  " + str(costo))
                    print("Lote C totalemente regado")

                else:
                    print("**********Ninguna accion que realizar**********")
                    print("El valor del costo actual es:  " + str(costo))
