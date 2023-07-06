def fibonacci(n):
    raiz_de_5 = 5**(0.5)
    u = 1/raiz_de_5
    x1 = (1 + raiz_de_5)/2
    x2 = (1 - raiz_de_5)/2
    x1 = x1**n
    x2 = x2**n
    v = (x1 - x2)//raiz_de_5
    return v

print(fibonacci(2))

def euclides(a, b):
    while b != 0:
        a, b = b, a%b
    return a
def euclides_estendido(a, b):
    if b == 0:
        return a, 0, 1
    else:
        mdc, x, y = euclides_estendido(b, a%b)
        return mdc, y-(a//b)*x, x
