def L(n, x, k, xv):
    saidaN = saidaD = 1
    for i in range(k):
        saidaN *= (x - xv[i])
        saidaD *= (xv[k] - xv[i])
    for i in range(k+1, n):
        saidaN *= (x - xv[i])
        saidaD *= (xv[k] - xv[i])
    return saidaN/saidaD


def Lagrange(x, xv, yv):
    saida = 0
    n = len(xv)
    for i in range(n):
        saida += yv[i]*L(n, x, i, xv)
    return saida


xv, yv, x = [-3, -2, 1, 3], [-1, 2, -1, 10], 2
print(Lagrange(x, xv, yv))
xv, yv, x = [-1, 0, 2], [4, 1, -1], 1
print(Lagrange(x, xv, yv))
