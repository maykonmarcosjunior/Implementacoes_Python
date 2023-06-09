import math


def f(x):
    return ((math.e)**x) - 2*(math.cos(x))


def r(a, b, p, flag):
    if not flag:
        return a - (f(a)*(b - a) / (f(b) - f(a)))
    elif flag == 1:
        return a - (p*f(a)*(b - a) / (f(b) - p*f(a)))
    else:
        return a - (f(a)*(b - a) / (p*f(b) - f(a)))


def p(x1, x0):
    return f(x1) / (f(x1) + f(x0))


def falsa_pos(a, b):
    k, erro = 0, f(a)
    while math.fabs(erro) > 10**(-15):
        k += 1
        m = r(a, b, 0, 0)
        if erro*f(a) < 0:
            m = r(a, m, p(b, m), 1)
            b = m
        else:
            m = r(m, b, p(a, m), 2)
            a = m
        erro = f(m)
    return k, m, erro


a, b = 0, 2

k, m, erro = falsa_pos(a, b)

print(k, "iterações, x =", m, "f(x) =", erro)
