import gauss
import print_file


def interpola(x, y, x0):
    n = len(x)
    A = [0]*n
    for i in range(n):
        A[i] = [1]*n
        for j in range(1, n):
            A[i][j] = x[i]**j
    F = gauss.gauss_sem_pivo(A, y)
    x1 = F[0]
    for i in range(1, n):
        x1 += F[i]*(x0**i)
    return x1


x = [-3, -2, 1, 3]
y = [-1, 2, -1, 10]

x = [-1, 0, 1]
y = [4, 1, -1]
x0 = 2

x1 = interpola(x, y, x0)

print("f(x) =", x1)
