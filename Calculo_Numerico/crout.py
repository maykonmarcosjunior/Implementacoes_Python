import print_file


def crout(A, b):
    n = len(b)
    L = [0]*n
    U = [0]*n
    for i in range(n):
        L[i] = [0]*n
        U[i] = [0]*n
        U[i][i] = 1

    for k in range(n):
        for i in range(k, n):
            j = i + 1
            if j == n:
                j = i
            LL = A[i][k]
            UU = A[k][j]
            for r in range(i):
                LL -= L[i][r]*U[r][k]
                UU -= L[k][r]*U[r][j]
            L[i][k] = LL
            if j != i:
                U[k][j] = UU / L[k][k]

    y = [0]*n
    x = [0]*n

    for i in range(n):
        YY = b[i]
        for j in range(0, i):
            YY -= L[i][j]*y[j]
        y[i] = YY/L[i][i]

    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j]*x[j]

    r = [0]*n

    for i in range(n):
        r[i] = b[i]
        for j in range(n):
            r[i] -= A[i][j]*x[j]

    return L, U, y, x, r


A = [
    [1, -2, 7, 2],
    [2, 5, -3, 1],
    [9, -6, 4, 1],
    [4, -3, -6, 7]
]
b = [-18, 31, 35, 15]

L, U, y, x, r = crout(A, b)

printar(L, U, y, x, r)
