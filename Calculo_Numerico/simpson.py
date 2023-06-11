import math


def f(x):
    return math.exp(x)


def simpson(a, b):
    h = (b - a)/2
    saida = f(a) + 4*f(a+h) + f(b)
    return saida*(h/3)


def simpson_composto(a, b, n):
    if not n % 2 == 0:
        return "N deve ser par"
    h = (b - a)/n
    saida0 = saida1 = 0
    N = n//2
    for i in range(1, N):
        saida0 += f(a + (2*i - 1)*h)
        saida1 += f(a + 2*i*h)
    saida0 += f(b - h)
    saida = f(a) + f(b) + 4*saida0 + 2*saida1
    return saida*(h/3)


def simpson_preciso(a, b, erro):
    margem = simpson(a, b)
    fx = - margem
    n = 4
    while abs(margem - fx) > erro:
        margem = fx
        fx = simpson_composto(a, b, n)
        n += 2
    return fx


a, b, n, erro = 0, 1, 4, 10**(-16)

print("Fórmula Simples =", simpson(a, b))
print("Fórmula Composta =", simpson_composto(a, b, n))
print("Fórmula Precisa =", simpson_preciso(a, b, erro))
print("exato =", math.exp(1) - math.exp(0))
