import math


def f(x):
    return math.e**x - 2*math.cos(x)


def sec(a, b):
    return (f(a) - f(b)) / (a - b)


def secante(a, b, erro):
    k = 0
    while math.fabs(f(a)) > erro:
        k += 1
        c = a
        a = (a - (f(a) / sec(a, b)))
        b = c
    return a, k


a, b, erro = 0, 2, 10**(-15)

x, k = secante(a, b, erro)

print(k, "iterações")
print("x =", x)
print("f(x) =", f(x))
