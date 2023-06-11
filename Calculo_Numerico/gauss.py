def pivota(inicio, n, A, indices):
    max, k = abs(A[indices[inicio]][inicio]), inicio
    for i in range(inicio+1, n):
        if abs(A[indices[i]][inicio]) > max:
            max = abs(A[indices[i]][inicio])
            k = i
    indices[inicio], indices[k] = indices[k], indices[inicio]


def gauss_sem_pivo(A, b):
    n = len(b)
    indices = [i for i in range(n)]
    for k in range(n):
        pivota(k, n, A, indices)
        for i in range(k+1, n):
            m = A[indices[i]][k]/A[indices[k]][k]
            b[indices[i]] -= m*b[indices[k]]
            for j in range(k, n):
                A[indices[i]][j] -= m*A[indices[k]][j]
    x = [0]*n
    for i in range(n-1, -1, -1):
        var = b[indices[i]]
        for j in range(i+1, n):
            var -= A[indices[i]][j]*x[indices[j]]
        x[indices[i]] = var/A[indices[i]][i]
    return [x[i] for i in indices]
