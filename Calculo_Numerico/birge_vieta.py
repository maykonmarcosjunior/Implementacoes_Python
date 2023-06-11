import math


def birge_vieta(a, x0, erro):
    n = len(a)
    k = 0
    b = [a[0]]*n
    c = [a[0]]*(n-1)
    while math.fabs(b[n-1]) > erro:
        k += 1
        for i in range(1, n-1):
            b[i] = b[i-1]*x0 + a[i]
            c[i] = c[i-1]*x0 + b[i]
        b[n-1] = b[n-2]*x0 + a[n-1]
        x0 -= b[n-1]/c[n-2]
    return k, x0, b


a = [1, -9, 27, -31, 12]
erro = 10**(-8)
x0 = 6

k, x0, b = birge_vieta(a, x0, erro)

print(k, "iterações")
print("x =", x0)
print("r =", b[-1])
