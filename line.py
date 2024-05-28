import math 
import numpy as np
import matplotlib as mp

def ejeX(a, b, c):
    for i in range(int(c)):
        aux1 = b * float(i)
        aux2 = a + aux1
        aux3 = 100 * aux2
        aux4 = math.floor(aux3)
        aux5 = aux4 / 100
        print("")
        print(f"Vuelta {i} de resultados del eje x: {aux5}")

def ejeY(a, b, c):
    for i in range(int(c)):
        aux1 = b * float(i)
        aux2 = a + aux1
        aux3 = 100 * aux2
        aux4 = math.floor(aux3)
        aux5 = aux4 / 100
        print("")
        print(f"Vuelta {i} de resultados del eje y: {aux5}")

def bucle(a, b, c, d, e, f, g):
    print("")
    print("COMIENZO DATOS EJE X")
    ejeX(a, e, g)
    print("")
    print("COMIENZO DATOS EJE Y")
    ejeY(b, f, g)

def cuad(x):
    return x * x

def PAUSE():
    input("Presione enter para comenzar a ingresar las coordenadas")

def main():
    PAUSE()

    p = float(input("Ingrese el paso: "))
    X0 = float(input("Ingrese el punto X inicial: "))
    Y0 = float(input("Ingrese el punto Y inicial: "))
    XN = float(input("Ingrese el punto X final: "))
    YN = float(input("Ingrese el punto Y final: "))

    # Pitágoras
    a = XN - X0
    c = cuad(a)

    b = YN - Y0
    d = cuad(b)

    D = math.sqrt(c + d)  # Hipotenusa

    Z = D / p
    N1 = math.floor(Z) + 1
    N0 = math.floor(Z)
    pY = (YN - Y0) / N0
    pX = (XN - X0) / N0

    if X0 == 0 and Y0 == 0 and XN == 0 and YN == 0:
        print("")
        print("Los datos ingresados son nulos")
    else:
        bucle(X0, Y0, XN, YN, pX, pY, N1)

if __name__ == "__main__":
    main()
