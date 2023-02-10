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
            break
    if Opcion not in listaOpciones:
            print("\n¡¡Digite Opción correcta!!")
            continue
    else:
        if Opcion=="0" or Opcion== "salir" or Opcion == "SALIR":
            break
print("Fin del programa")
