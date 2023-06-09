import math


def f(x):
    return ((math.e)**x) - 2*(math.cos(x))


def r(a, b):
    return a - (f(a)*(b - a) / (f(b) - f(a)))


def falsa_posicao(a, b):
    k, erro = 0, f(a)
    while math.fabs(erro) > 10**(-15):
        k += 1
        m = r(a, b)
        erro = f(m)
        if erro*f(a) < 0:
            b = m
        else:
            a = m
    return k, m, erro


k, m, erro = falsa_posicao(0, 2)

print(k, "iterações, x =", m, "f(x) =", erro)
