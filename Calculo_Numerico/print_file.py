def printFloat(x):
    print("%.5f" % x, end=' ')


def printR(r, n):
    print("r =")
    for i in range(n):
        printFloat(r[i])
    print("\n")


def confere(A, b, x, n, indices=[], erro=0):
    if len(indices) != n:
        indices = [i for i in range(n)]
    r = [i for i in b]
    print("conferindo:")
    for i in range(n-1, -1, -1):
        temp = 0
        for j in range(n-1, -1, -1):
            temp += A[indices[i]][j]*x[j]
        print("b[%d] =" % i, end=' ')
        printFloat(b[indices[i]])
        print(" ≃ ", end='')
        printFloat(temp)
        print()
        r[indices[i]] -= temp
    print()
    printR(r, n)
    print("erro =", erro)


def printA(A, n):
    print("Matriz =")
    for i in range(n):
        for j in range(n):
            printFloat(A[i][j])
        print('\n\n')
    print()


def printB(b, n):
    print("b =")
    for i in range(n):
        printFloat(b[i])
    print("\n")


def printX(x, n):
    print("x =")
    for i in range(n):
        printFloat(x[i])
    print("\n")


def printIndices(o, n):
    print("índices =", end=' ')
    for i in range(n):
        print('%d' % (o[i]), end=' ')
    print("\n")


def printar(A, b, x, flag0=0, o=[], flag1=0):
    n = len(b)
    printA(A, n)
    printB(b, n)
    printX(x, n)
    if flag0 == 1:
        confere(A, b, x, n, o)
    if flag1 == 1:
        printIndices(o, n)
