from quad_arquivo import Narquivo
import math


def f(x):
    return (x**3)/3


def integral(x):
    return (x**4)/12


def quadratura(a, b, n):
    N = Narquivo[n]
    A = N[0]
    t = N[1]
    dx = (b-a)/2
    saida = 0
    for i in range(n):
        x = t[i]*dx + (b+a)/2
        saida += A[i]*f(x)*dx
    return saida


a, b, n = 2, 6, 2

print("quadratura =", quadratura(a, b, n))
print("exato =", integral(b) - integral(a))
