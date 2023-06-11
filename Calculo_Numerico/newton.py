import math


def f(x):
    return (math.e)**x - 4*x*x


def df(x):
    return (math.e)**x - 8*x


def Newton(x0, erro):
    k = 0
    m = x0
    while math.fabs(f(m)) >= erro:
        m = m - f(m)/df(m)
        k += 1
    return m, k


x0, erro = 1, 10**(-6)

x, k = Newton(x0, erro)

print(k, "iterações")
print("resultado final:")
print("x =", x)
print("f(x) =", f(x))
