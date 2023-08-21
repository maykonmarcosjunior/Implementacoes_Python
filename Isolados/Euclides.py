from Isolados.Euclides import euclides_extendido


def fibonacci(n):
    raiz_de_5 = 5**(0.5)
    x1 = (1 + raiz_de_5)/2
    x2 = (1 - raiz_de_5)/2
    v = x1**n - x2**n
    v = v//raiz_de_5
    return v


def mdc(a, b):
    while b:
        a, b = b, a % b
    return a


def mmc(a, b):
    final_a, final_b = a, b
    while b:
        a, b = b, a % b
    return (final_a*final_b) // a


def euclides_extendido(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = (a // b), b, (a % b)
        x0, x1 = x1, (x0 - q * x1)
        y0, y1 = y1, (y0 - q * y1)
    return a, x0, y0


def euclides_extendido_rec(a, b):
    if b == 0:
        return a, 0, 1
    else:
        mdc, x, y = euclides_extendido(b, a % b)
        return mdc, y-(a//b)*x, x
