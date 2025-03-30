def change():

    gasto = float(input("Ingresar gasto:"))
    recibido = float(input("Ingresar dinero recibido:"))
    pesos = (recibido - gasto)
    print (f"{"gasto:"} {gasto}")
    print (f"{"recibido:"} {recibido}")
    print ("")
    print ("Vuelto")
    print ("")
    print (f"{"Pesos:"} {int(pesos)}")
    print (f"{"Centavos:"} {(int(pesos * 100) %100)}")
    print ("fin del programa")
change ()
