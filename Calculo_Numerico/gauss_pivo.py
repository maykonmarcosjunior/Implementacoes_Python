from print_file import printar


def pivota(inicio, n, A, b, indices):
    max, k = abs(A[inicio][inicio]), inicio
    for i in range(inicio, n):
        if abs(A[i][inicio]) > max:
            max = abs(A[i][inicio])
            k = i
    A[inicio], A[k] = A[k], A[inicio]
    b[inicio], b[k] = b[k], b[inicio]
    indices[inicio], indices[k] = indices[k], indices[inicio]


def gauss(A, b):
    n = len(b)
    indices = [i for i in range(n)]
    for k in range(n):
        pivota(k, n, A, b, indices)
        for i in range(k+1, n):
            m = A[i][k]/A[k][k]
            b[i] -= m*b[k]
            for j in range(k, n):
                A[i][j] -= m*A[k][j]

    x = [0]*n
    for i in range(n-1, -1, -1):
        var = b[i]
        for j in range(i+1, n):
            var -= A[i][j]*x[j]
        x[i] = var/A[i][i]
    printar(A, b, x, n, 1, indices, 1)


flag = 1

if flag == 0:
    A = [
        [1, 1, 1.5, 1, 1.5, 0, 0, 0, 0, 0],
        [0, 1, 0.01, 0.51, 1.5, 0.5, 0, 0, 0, 0],
        [2.9, 1, 2, 1, 1, 0, 5, 0, 0, 0],
        [9, 1, 0.2, 1, 1, 0, 0, 1.5, 0, 0],
        [1, 0, 2, 0, 0, 1, 1, 1, 0, 2],
        [0, 1, 0, 0, -2, 0, 1, -1, 1, 1],
        [1, 0, 2, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 2, 0, 1, 1, 1, -1],
        [0, 0, 1, 0, 2, 1, -1, 0, -1, -1],
        [0, 1, 0, 0, 2, 0, 1, 0, 1, 1,]
    ]
    b = [4, -3, 1, -1, -1, 0, -1, 1, 3, -2]
elif flag == 1:
    A = [
        [1, 1, 0, 1],
        [2, 1, -1, -1],
        [-1, -2, 3, -1],
        [3, -1, -1, 2]
    ]
    b = [2, 1, 4, -3]

gauss(A, b)
