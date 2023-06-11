import math
import gauss
import print_file


def h(x, k):
    return x**k


def ln(x):
    return math.log(x)


def e(x):
    return math.exp(x)


def ajuste_exp(x, y):
    n = len(x)
    A = [[n, 0], [0, 0]]
    b = [0, 0]
    g = [0]*n
    z = [ln(yy) for yy in y]
    for i in range(n):
        A[0][1] += x[i]
        A[1][0] += x[i]
        b[0] += z[i]
        A[1][1] += x[i]**2
        b[1] += z[i]*x[i]
    Acopia = [[a for a in aa] for aa in A]
    c = gauss.gauss_sem_pivo(Acopia, [b[0], b[1]])
    erro = 0
    for i in range(n):
        g[i] = c[0] + c[1]*ln(x[i])
        erro += (y[i] - e(g[i]))**2
    c[0] = e(c[0])
    return A, b, c, erro**(0.5)


x = [i for i in range(1, 5)]
y = [2*(i**2) for i in x]

A, b, c, erro = ajuste_exp(x, y)
printar(A, b, c, erro)
