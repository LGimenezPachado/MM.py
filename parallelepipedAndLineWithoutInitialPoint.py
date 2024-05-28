import math

# DEFINITION OF FUNCTIONS


def line(m, n, o, p, q):
    # Pythagoras
    a = o - m
    c = cuad(a)

    b = p - n
    d = cuad(b)

    D = math.sqrt(c + d)  # Hypotenuse

    Z = D / q
    N1 = math.floor(Z) + 1
    N0 = math.floor(Z)
    pX = (o - m) / N0
    pY = (p - n) / N0

    if m == 0 and n == 0 and o == 0 and p == 0:
        print("\nThe data entered is null")
    else:
        line_loop(m, n, o, p, pX, pY, N1)

# BEGIN OF PARALLELEPIPED DETERMINATION


def flat_seq(a, b, c, d, e, f, g, h, i):
    # Consists of one or more subdiagrams, or frames, that execute sequentially.
    # Use the Flat Sequence structure to ensure that a subdiagram executes before or after another subdiagram.

    # first out
    aux1 = a + e
    aux2 = aux1 + g
    print("first output:", aux2)

    # second out
    aux3 = b + f
    aux4 = aux2 + h
    print("second output:", aux4)

    # third out
    aux5 = c - e
    aux6 = aux5 + g
    print("third output:", aux6)

    # fourth out
    aux7 = d - f
    aux8 = aux7 + h
    print("fourth output:", aux8)

    line(aux2, aux4, aux6, aux8, i)


def loop(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    # getting ready X2
    aux1 = c + e
    aux2 = aux1 - a

    # getting ready Y2
    aux3 = f + d
    aux4 = aux3 - b

    for iC in range(int(g) + 1):
        aux1 = h * iC
        aux2 = j * iC
        aux3 = i * iC
        aux4 = k * iC

        print("")

        pcntaje = float(iC) / float(g) * 100

        if iC == 0:
            print("\ninitial point // [{}% realized]\n".format(pcntaje))
            flat_seq(a, b, c, d, aux1, aux2, aux3, aux4, n)
            print("\n")

        elif pcntaje != 100 and iC > 0:
            print("round number {} // [{}% realized]\n".format(iC, pcntaje))
            flat_seq(a, b, c, d, aux1, aux2, aux3, aux4, n)
            print("\n")

        elif pcntaje == 100:
            print("final round // [{}% realized]\n".format(pcntaje))
            flat_seq(a, b, c, d, aux1, aux2, aux3, aux4, n)
            print("\n")


def cuad(x):
    return x * x


def cmp(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    else:
        print("the values are the same")
        return 0

# END OF PARALLELEPIPED DETERMINATION

# BEGIN OF LINE WITHOUT INITIAL POINT DETERMINATION


def x_axis(a, b, c):
    for i in range(int(c)):
        aux1 = b * float(i)
        aux2 = a + aux1
        aux3 = 100 * aux2
        aux4 = math.floor(aux3)
        aux5 = aux4 / 100
        print("round {} of x axis results {}".format(i, aux5))


def y_axis(a, b, c):
    for i in range(int(c)):
        aux1 = b * float(i)
        aux2 = a + aux1
        aux3 = 100 * aux2
        aux4 = math.floor(aux3)
        aux5 = aux4 / 100
        print("round {} of y axis results: {}".format(i, aux5))

    print("")
    print("///////////////////////////////////////////////////////")


def line_loop(a, b, c, d, e, f, g):
    print("\nx axis begin")
    x_axis(a, e, g)
    print("\ny axis begin")
    y_axis(b, f, g)

# END OF LINE WITHOUT INITIAL POINT DETERMINATION


def main():
    p = float(input("enter distance value: "))

    if p >= 0:
        X0 = float(input("enter X0 value: "))
        Y0 = float(input("enter Y0 value: "))
        X1 = float(input("enter X1 value: "))
        Y1 = float(input("enter Y1 value: "))
        X2 = float(input("enter X2 value: "))
        Y2 = float(input("enter Y2 value: "))

        print("\n///////////////////////////////////////////////////////\n")

        # X1
        a = X1 - X0
        c = cuad(a)

        b = Y1 - Y0
        d = cuad(b)

        D1 = math.sqrt(c + d)
        Z1 = D1 / p
        N1 = math.floor(Z1) + 1



        dX1 = (X1 - X0) / (N1 - 1)
        dY1 = (Y1 - Y0) / (N1 - 1)

        # X2
        e = X2 - X0
        g = cuad(e)

        f = Y2 - Y0
        h = cuad(f)

        D2 = math.sqrt(g + h)
        Z2 = D2 / p
        N2 = math.floor(Z2) + 1

        dX2 = (X2 - X0) / (N2 - 1)
        dY2 = (Y2 - Y0) / (N2 - 1)

        # TOTAL
        p1 = D1 / (N1 - 1)
        p2 = D2 / (N2 - 1)

        N = cmp(N1, N2)

        loop(X0, Y0, X1, Y1, X2, Y2, N, dX1, dY1, dX2, dY2, p1, p2, p)

    else:
        print("\nthe value of the distance cannot be negative")

if __name__ == "__main__":
    main()
