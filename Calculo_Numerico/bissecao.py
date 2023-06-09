import math


def f(x):
    return (math.e)**x - 2*math.cos(x)


def bissecao(a, b):
    k = 0
    erro = f(a)
    while math.fabs(erro) >= 10**(-6):
        k += 1
        m = (a+b)/2
        erro = f(m)
        if f(a)*erro < 0:
            b = m
        else:
            a = m
    return k, m, erro


a, b = 0, 2

k, x, erro = bissecao(a, b)

print(k, "iterações")
print("resultado final:")
print("x =", x)
print("f(x) =", erro)
