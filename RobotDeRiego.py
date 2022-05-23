#Creamos una funcion que permite definir un bloque de código reutilizable que se puede ejecutar muchas veces dentro de tu programa.
def robot(): 
  
  estadoObjetivo = {'A': '0', 'B':  '0', 'C': '0'}  #El robot completa el objetivo si todos los lotes estan regados
  #Inicializmos una variable para el costo.
  costo = 0
  #Mostramos por pantalla que opciones va a tener el usuario
  print('''   Estimado usuario recuerde que las ubicaciones están dadas de la siguinte manera
  [Lote_1 = A]
  [Lote_2 = B]
  [Lote_3 = c] '''  
  )
  #Se muestra por pantallo los lotes disponibles y un mensaje para elegir que opciones quiere.
  print('''Esimado usuario digite la ubicacion donde se encunetra el robot 
  [Lote_1]
  [ Lote_2]
  [Lote_3]''')
  ubicacionLote = input("Digite donde se encuentra el robot:  ") #Le pedimos al usuario que digite donde se encuentra el robot, este dato es de tipo string
  # '''
  # Para la primera sentencia if, se lee que si el usuario digita la opciones A el robot se encuentra en el lote 1
  # '''
  if ubicacionLote == 'A':
      print("El robot se encunetra en la ubicación:  A")
      estadoDelLoteA = input("Digite el estado del lote:   "  + ubicacionLote)
      estadoLoteB = input("Digite el estado del lote B:    ")
      estadoLoteC = input("Digite el estado del lote  C:    ")
      