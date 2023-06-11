import math
import gauss
import print_file


def h(x, k):
    return x**k


def ajuste(x, y, M):
    n = len(x)
    A = [0]*(M+1)
    b = [0]*(M+1)
    g = [0]*n
    for i in range(M+1):
        A[i] = [0]*(M+1)
        for k in range(n):
            for j in range(M+1):
                A[i][j] += h(x[k], i)*h(x[k], j)
            b[i] += y[k]*h(x[k], i)
    Acopia = [[a for a in aa] for aa in A]
    c = gauss.gauss_sem_pivo(Acopia, [bb for bb in b])
    erro = 0
    for i in range(n):
        for j in range(M+1):
            g[i] += c[j]*h(x[i], j)
        erro += (y[i] - g[i])**2
    return A, b, c, erro**(0.5)


M = 1
x = [1.3, 3.4, 5.1, 6.8, 8]
y = [2, 5.2, 3.8, 6.1, 5.8]
'''
M = 1
x = [1 + (0.2)*i for i in range(21)]
y=[-1.945, -1.253, -1.140, -1.087,
   -0.760, -0.682, -0.424, -0.012,
   -0.190,  0.452,  0.337,  0.764,
    0.532,  1.073,  1.286,  1.502,
    1.582, 1.993,   2.473,  2.503,
    2.322]
'''
M = 1
x = [0, 20, 40, 60, 100]
y = [81.4, 77, 7, 74.2, 72.4, 70.3, 68.8]
A, b, c, erro = ajuste(x, y, M)

printar(A, b, c, erro)
