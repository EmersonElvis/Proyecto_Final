import numpy as np

def IngresarElementoMatriz(Fila,Columna):
    Matriz = []
    for i in range(Fila):
        Fila_x = []
        for j in range(Columna):
            while True:
                try:
                    Elemento = float(input("Elemento (%d,%d): " %(i,j)))
                except:
                    continue
                break
            Fila_x.append(Elemento)
        Matriz.append(Fila_x)
    return Matriz

def Pedir_ValidarDatoEntero(FilaColumna):
    while True:
        try:
            fila_columna = int(input(f"{FilaColumna}:").lower().replace(" ",""))
        except :
            print("¡¡Digite bien!!")
            continue
        return fila_columna

def sumaMatrices():
    print("\n\tSuma de dos Matrices")
    Fila = "Fila" ; Columna = "Columna"
    print("\nPara la primera Matriz")
    Filax = Pedir_ValidarDatoEntero(Fila) ; Columnax = Pedir_ValidarDatoEntero(Columna)
    print("\nPara la segunda Matriz")
    Filay = Pedir_ValidarDatoEntero(Fila) ; Columnay = Pedir_ValidarDatoEntero(Columna)
    if Columnax == Columnay and Filax == Filay:
        print("Llenando primera Matriz...")
        MatrizA=IngresarElementoMatriz(Filax,Columnax) ; Matriz1 = np.array(MatrizA)
        print("Llenando segunda Matriz...")
        MatrizB=IngresarElementoMatriz(Filay,Columnay) ; Matriz2 = np.array(MatrizB)
        Suma =[]
        for i in range (Filax):
            Suma.append( [0] * Columnax)
            for j in range(Columnax):
                Suma[i][j] += MatrizA[i][j] + MatrizB[i][j]

        resultado = np.array(Suma)
        print("\n\tMatriz A\n", Matriz1)
        print("\n\tMatriz B\n", Matriz2)
        print("\nLa suma de las matrices es:")
        print(resultado)
    else:
        print("Recuerde la suma entre dos matrices debe ser de la misma dimension de filas y columnas")
#RESTA DE MATRICES
def restaMatrices():
    print("\n\tSuma de dos Matrices")
    Fila = "Fila" ; Columna = "Columna"
    print("\nPara la primera Matriz")
    Filax = Pedir_ValidarDatoEntero(Fila) ; Columnax = Pedir_ValidarDatoEntero(Columna)
    print("\nPara la segunda Matriz")
    Filay = Pedir_ValidarDatoEntero(Fila) ; Columnay = Pedir_ValidarDatoEntero(Columna)
    if Columnax == Columnay and Filax == Filay:
        print("Llenando primera Matriz...")
        MatrizA=IngresarElementoMatriz(Filax,Columnax) ; Matriz1 = np.array(MatrizA)
        print("Llenando segunda Matriz...")
        MatrizB=IngresarElementoMatriz(Filay,Columnay) ; Matriz2 = np.array(MatrizB)
        Resta =[]
        for i in range (Filax):
            Resta.append( [0] * Columnax)
            for j in range(Columnax):
                Resta[i][j] += MatrizA[i][j] - MatrizB[i][j]

        resultado = np.array(Resta)
        print("\n\tMatriz A\n", Matriz1)
        print("\n\tMatriz B\n", Matriz2)
        print("\nLa resta de las matrices es:")
        print(resultado)
    else:
        print("Recuerde la resta entre dos matrices debe ser de la misma dimension de filas y columnas")

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
    [0] SALIR """)
    Opcion=input("--->").lower().replace(" ", "")
    listaOpciones=["P", "S", "R","I","D","0","p","s","r","i","d", "PRODUCTO", "SUMA", "RESTA", "INVERSA", "DETERMINANTE",
                   "producto","suma","resta","inversa","determinante"]
    while Opcion in listaOpciones:
        if Opcion =="P" or Opcion=="p" or Opcion=="PRODUCTO" or Opcion=="producto":
            #ProductoMatrices()
            break
        elif Opcion=="S" or Opcion=="s" or Opcion=="SUMA" or Opcion=="suma":
            sumaMatrices()
            break
        elif Opcion =="R" or Opcion=="r" or Opcion=="RESTA" or Opcion=="resta":
            restaMatrices()
            break
        elif Opcion=="I" or Opcion=="i" or Opcion=="INVERSA" or Opcion=="inversa":
            #inversamatrices()
            break
        elif Opcion=="D" or Opcion=="d" or Opcion=="DETERMINANTE" or Opcion=="determinante":
            #determinantematrices()
            break
    if Opcion not in listaOpciones:
            print("\n¡¡Digite Opción correcta!!")
            continue
    else:
        if Opcion=="0" or Opcion== "salir" or Opcion == "SALIR":
            break
print("Fin del programa")