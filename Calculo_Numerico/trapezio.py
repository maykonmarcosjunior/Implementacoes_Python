import math


def f(x):
    return math.exp(x)


def trapezio(a, b):
    return (f(b) + f(a))*(b - a)/2


def trapezio_composto(a, b, n):
    h = (b - a)/n
    saida = 0
    for i in range(1, n):
        saida += f(a + i*h)
    saida *= 2
    saida = saida + f(a) + f(b)
    return saida*h/2


def trapezio_preciso(a, b, erro):
    margem = trapezio(a, b)
    fx = - margem
    n = 2
    while abs(margem - fx) > erro:
        margem = fx
        n += 2
        fx = trapezio_composto(a, b, n)
    return fx, n


a, b, n, erro = 0, 1, 30320, 10**(-16)

print("Formula Simples =", trapezio(a, b))
print("Formula Composta =", trapezio_composto(a, b, n))
print("Formula Precisa =", trapezio_preciso(a, b, erro))
print("exato =", math.exp(1) - math.exp(0))
