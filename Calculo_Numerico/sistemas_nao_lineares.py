import math
import gauss


def F(X):
    R = [
        X[0]*2 - X[1] - math.exp(- X[0]),
        X[1]*2 - X[0] - math.exp(- X[1]),
    ]
    return R


def J(X, derivada=False):
    if derivada:
        R = [
            [2 + math.exp(-X[0]), -1],
            [-1, 2 + math.exp(-X[1])],
        ]
    else:
        R = Secante(X)
    return R


def Secante(X, h=10**(-12)):
    N = len(X)
    R = [0]*N
    FX = F(X)
    for i in range(N):
        R[i] = [0]*N
    for i in range(N):
        temp_X = [x for x in X]
        temp_X[i] += h
        temp_FX = F(temp_X)
        for j in range(N):
            R[j][i] = (temp_FX[j] - FX[j])/h
    return R


def sistema(X, erro):
    n = len(X)
    D = gauss.gauss_sem_pivo(J(X), F(X))
    flag = True
    for i in range(n):
        X[i] -= D[i]
        flag = flag and (abs(D[i]) < erro)
    return X, flag


def Newton(X, erro):
    k = 0
    flag = False
    while not flag:
        k += 1
        X, flag = sistema(X, erro)
    return k, X


x = [-5, -5]
erro = 10**(-8)
k, X = Newton(x, erro)
print("tentativas:", k)
print("X =\n", X)
print(F(X)[0])
print(F(X)[1])
