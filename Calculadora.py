def matrizTranspuesta():

    filas_MatrizA=  int(input("Ingrese la cantidad de filas de la matriz A => "))
    columnas_MatrizA=  int(input("Ingrese la cantidad de columnas de la matriz A=> "))
    print("La matriz que usted acaba de introdducir es de orden ", filas_MatrizA,"*", columnas_MatrizA)
#creando una matriz inicial
    matrizA  = []
    for i in range(filas_MatrizA):
        matrizA.append([0]* columnas_MatrizA)

#rellenando la matriz A
    for fila in range(filas_MatrizA):
        for columna in range(columnas_MatrizA):
        #usemos excepciones para evitar errores no previstos, es error si el usuaario introduce
        # un dato que no sea numerico
            while True:
                try:
                    matrizA[fila][columna]= float(input(f'Ingrese el valor en la posicion  {fila+1},{columna+1}: '))
                    break
                except ValueError:
                    print('Solo es admisible valores numericos, intente de nuevo => ')#mensaje para poer un numero

#mostrando la matrizA
    print('\nMatriz A \n')
    for i in matrizA:
        print(i)

 # otra matriz vacia para aalmacenar la operacion transpuesta a realizar
    matrizTranspuesta = []
    for i in range(columnas_MatrizA):
        matrizTranspuesta.append([0]* filas_MatrizA)

    for fila in range(columnas_MatrizA):
            for columna in range(filas_MatrizA):
                matrizTranspuesta[fila][columna] = matrizA[columna][fila] #es transpuesta cuando se cambia las filas por las columnas

#imprimir la matriz transpuesta, que es la matriz inicial, cambiadaa las fials por columnasa y columnas por filas
    print('\nMatriz Transpuesta de A \n')
    for i in matrizTranspuesta:
        print(i)

#Menú General
while True:
    #print("\tBIENVENIDO")
    print("\n\tCALCULADORA DE MATRICES")
    print("""
    [P] PRODUCTO
    [S] SUMA
    [R] RESTA
    [I] INVERSA
    [D] DETERMINANTE
    [T] TRANSPUESTA
    [0] SALIR """)
    Opcion=input("--->").lower().replace(" ", "")
    listaOpciones=["P", "S", "R","I","D","T","p","s","r","i","d","t", "PRODUCTO", "SUMA", "RESTA", "INVERSA", "DETERMINANTE",
                   "TRANSPUESTA","producto","suma","resta","inversa","determinante","transpuesta",]
    while Opcion in listaOpciones:
        if Opcion =="P" or Opcion=="p" or Opcion=="PRODUCTO" or Opcion=="producto":
            #ProductoMatrices()
            break
        elif Opcion=="S" or Opcion=="s" or Opcion=="SUMA" or Opcion=="suma":
            #sumaMatrices()
            break
        elif Opcion =="R" or Opcion=="r" or Opcion=="RESTA" or Opcion=="resta":
            #restaMatrices()
            break
        elif Opcion=="I" or Opcion=="i" or Opcion=="INVERSA" or Opcion=="inversa":
            #inversamatrices()
            break
        elif Opcion=="D" or Opcion=="d" or Opcion=="DETERMINANTE" or Opcion=="determinante":
            #determinantematrices()
            break
        elif Opcion=="T" or Opcion=="t" or Opcion=="TRANSPUESTA" or Opcion=="transpuesta":
            #matrizTranspuesta()
            print("mostrando matriz transpuesta /.....")
            matrizTranspuesta()
            break
    if Opcion not in listaOpciones:
            print("\n¡¡Digite Opción correcta!!")
            continue
    else:
        if Opcion=="0" or Opcion== "salir" or Opcion == "SALIR":
            break
print("Fin del programa")
