import numpy as np
#a=[[1,2,3,4,5],[1,4,12,31,5],[1,2,4,7,6],[1,9,8,7,0],[10,11,12,13,16]]
#def calculatorDeterminantMatrix(matriz):
#    determinante = np.linalg.det(matriz)
#    return determinante
#print(calculatorDeterminantMatrix(a)) 

#Multiplicacion
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

#Funcion Multiplicacion
def ProductoMatrices():
    print("\n\tMultiplicación de dos Matrices")
    Fila = "Fila" ; Columna = "Columna"
    print("\nPara el primer Matriz")
    Filax = Pedir_ValidarDatoEntero(Fila) ; Columnax = Pedir_ValidarDatoEntero(Columna)
    print("\nPara el segundo Matriz")
    Filay = Pedir_ValidarDatoEntero(Fila) ; Columnay = Pedir_ValidarDatoEntero(Columna) 
    if Columnax == Filay:
        print("Llenando primer Matriz...")
        MatrizA=IngresarElementoMatriz(Filax,Columnax) ; Matriz1 = np.array(MatrizA)
        print("Llenando segundo Matriz...")
        MatrizB=IngresarElementoMatriz(Filay,Columnay) ; Matriz2 = np.array(MatrizB)
        Producto =[]
        for i in range (len(MatrizA)):
            Producto.append([0]*len(MatrizB))
            for j in range (len(MatrizB[0])):
                for k in range (len(MatrizB)):
                    Producto[i][j] += MatrizA[i][k]*MatrizB[k][j]
        resultado = np.array(Producto)
        print("\n\tMatriz A\n", Matriz1)
        print("\n\tMatriz B\n", Matriz2)
        print("\nSu Producto de las matrices es:")
        print(resultado)
    else:
        print("Recuerde la multiplicación entre dos matrices debe ser mxn * nxp")
        

#Funcion Inversa
def mat(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz
def llenar(n):
    matriz=mat(n)
    for x in range(n):
        for y in range(n):
            matriz[x][y] = float(input(f"Valor de la fila {x+1} y columna {y+1}: "))
        respuesta.append(float(input("Valor de la constante de la ecuacion "+str(x+1)+" = " )))

def gjordan(n):
    for z in range(n-1,0,-1):
        for x in range (z):
            if (matriz[z][z]!=0):
                p =matriz[x][z]/matriz[z][z]
                matriz[x][z]=matriz[x][z]-(matriz[z][z]* p)
                respuesta[x]=respuesta[x]-(respuesta[z]*p)
def gaussJordan(n):
    for z in range(n-1,0,-1):
        for x in range(z):
            if (matriz[z][z] !=0 ):
                p= matriz[x][z]/matriz[z][z]
                matriz[x][z]=matriz[x][z]-(matriz[z][z]*p)
                respuesta[x]=respuesta[x] - (respuesta[z]*p)
def deter(n):
    det=1
    for x in range(n):
        det =matriz[x][x]*det
    print("\nEl valor de la determinante de la matriz es =",det)
#Programa   
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
class Matriz:
    def __init__(self,nfilas,ncolumnas):
        self.nfilas = nfilas
        self.ncolumnas = ncolumnas
        self.matriz=[]
        self.matrizMxN=False
        self.matriz_cuadrada=False
        self.operacion=""
    def optenerDatos(self):
        for i in range(0,self.nfilas):
            self.matriz.append([])
            for j in range(0,self.ncolumnas):
                while True:
                    try:
                        valor=int(input(f"Ingrese elemento de la matrix en la posicion {(i+1,j+1)}--> "))
                        break
                    except ValueError as e:
                        print("Ingesaste un caracter no válido vuelve a ingresar los valores. Error de tipo: {0}".format(e))

                self.matriz[i].append(valor)
        return self.matriz   
    def pedirDatos(dato):
            valor=-1
            while valor<0:
                try:
                    valor=int(input(dato))
                    if valor<0:
                        print("Los datos deben ser positivos.")
                except:
                    print("Ingresó un caracter no válido.")
            return valor
    def verificarMatriz(self):
        if self.nfilas==self.ncolumnas:
            self.matriz_cuadrada=True
            return self.matriz_cuadrada
    def MostrarMatriz(self):
      
        for i in range(self.nfilas): 
            print("[",end="")
            for j in range(self.ncolumnas):
                print(self.matriz[i][j],end="")
            print("]")
        print() 

def inversaM(self):
        self.MostrarMatriz()
        if self.verificarMatriz():
            return np.linalg.inv(self.matriz)
        else:
            return ("La matriz a ingresar debe ser 'cuadrada'")

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
    print("""\n\tCALCULADORA DE MATRICES\n
[P] PRODUCTO
[S] SUMA
[R] RESTA
[I] INVERSA
[D] DETERMINANTE
[T] TRANSPUESTA
[0] SALIR """)
    Opcion=input("--->").lower().replace(" ", "")
    listaOpciones=["P", "S", "R","I","D","T","p","s","r","i","d","t", "PRODUCTO", "SUMA", "RESTA", "INVERSA", "DETERMINANTE",
                   "TRANSPUESTA","producto","suma","resta","inversa","determinante","transpuesta"]
    while Opcion in listaOpciones:
        if Opcion =="P" or Opcion=="p" or Opcion=="PRODUCTO" or Opcion=="producto":
            ProductoMatrices()
            break
        elif Opcion=="S" or Opcion=="s" or Opcion=="SUMA" or Opcion=="suma":
            sumaMatrices()
            break
        elif Opcion =="R" or Opcion=="r" or Opcion=="RESTA" or Opcion=="resta":
            restaMatrices()
            break
        elif Opcion=="I" or Opcion=="i" or Opcion=="INVERSA" or Opcion=="inversa":
            inversaM(self)
            break
        elif Opcion=="D" or Opcion=="d" or Opcion=="DETERMINANTE" or Opcion=="determinante":
            n=int(input("Tamaño  de la matriz: "))
            matriz=[]
            respuesta=[]
            llenar(n)
            gjordan(n)
            gaussJordan(n)
            deter(n)
            break
        elif Opcion=="T" or Opcion=="t" or Opcion=="TRANSPUESTA" or Opcion=="transpuesta":
            print("mostrando matriz transpuesta /.....")
            matrizTranspuesta()
            break
    if Opcion=="0" or Opcion== "salir" or Opcion == "SALIR":
        break    
    else:
        if Opcion not in listaOpciones:
            print("\n¡¡Digite Opción correcta!!")
            continue
print("Fin del programa")
