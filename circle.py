import math

def cosF(X, Y, Z):
    aux_1 = math.cos(X)
    aux_2 = aux_1 * float(-Y)
    aux_3 = aux_2 / float(Z)
    aux_4 = aux_3 * 100
    aux_5 = math.floor(aux_4)
    aux_6 = aux_5 / 100
    return aux_6

def sinF(X, Y, Z):
    aux_1 = math.sin(X)
    aux_2 = aux_1 * float(Y)
    aux_3 = aux_2 / float(Z)
    aux_4 = aux_3 * 100
    aux_5 = math.floor(aux_4)
    aux_6 = aux_5 / 100
    return aux_6

def bucle(X, Y, A, B):
    sY, sA, sB = Y, A, B
    for i in range(X + 1):
        aux_1 = (2 * math.pi) / X
        AUX = i * aux_1
        cosFS = cosF(AUX, sY, sA)
        sinFS = sinF(AUX, sY, sB)
        pcntaje = float(i) / float(X) * 100

        if i == 0:
            print(f"initial point // [{pcntaje}% realized]")
            print(cosFS)
            print(sinFS)
        elif pcntaje != 100 and i > 0:
            print(f"round number {i} // [{pcntaje}% realized]")
            print(cosFS)
            print(sinFS)
            print("")
        elif pcntaje == 100:
            print(f"final round // [{pcntaje}% realized]")
            print(cosFS)
            print(sinFS)

    return 0

def main():
    p = int(input("Enter distance value: "))
    R = int(input("Enter radio value: "))
    XC = int(input("Enter XC value: "))
    YC = int(input("Enter YC value: "))

    per = 2 * math.pi * R
    Z = per / p
    N = math.floor(Z)

    print("")
    print(f"The flux will be repeated {N} times")
    print("")

    input("Press Enter to continue...")
    print("")

    bucle(N, R, XC, YC)

if __name__ == "__main__":
    main()
