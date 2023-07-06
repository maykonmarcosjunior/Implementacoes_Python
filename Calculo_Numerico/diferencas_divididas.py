def dif_div(ordem, xv, yv, i=0):
    if ordem == 0:
        return yv[i]
    saida = dif_div(ordem-1, xv, yv, i + 1)
    saida -= dif_div(ordem-1, xv, yv, i)
    saida /= (xv[i + ordem] - xv[i])
    return saida


def dif_div_n_rec(xv, yv):
    n = len(xv)
    A = [[yv[i] for i in range(n + j*0)] for j in range(n)]
    saida = [yv[0]]*n
    for i in range(1, n):
        for j in range(n-i):
            temp = (A[i-1][j+1] - A[i-1][j])
            A[i][j] = temp / (xv[j+i] - xv[j])
        saida[i] = A[i][0]
    return saida, A


def Newton_dif_div(xv, yv, x):
    n = len(xv)
    saida = 0
    DD, A = dif_div_n_rec(xv, yv)
    for i in range(n):
        termo = DD[i]
        for j in range(i):
            termo *= (x - xv[j])
        saida += termo
    return saida, A


xv, yv, x = [-3, -2, 1, 3], [-1, 2, -1, 10], 2
# print(Newton_dif_div(xv, yv, x))
xv, yv, x = [-1, 0, 2], [4, 1, -1], 1
xv, yv, x = [-3, -2, 1, 3], [-1, 2, -1, 10], 0
N, A = Newton_dif_div(xv, yv, x)
for i in A:
    print(i)
print(N)
