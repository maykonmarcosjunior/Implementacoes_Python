def gauss_seidel(A, b, erro, w=1):
    n = len(A)
    x = [0]*n
    k = 0
    margem = b[0]
    while abs(margem) >= erro:
        k += 1
        for i in range(n):
            x0 = x[i]
            x[i] = b[i]
            for j in range(i):
                x[i] -= A[i][j]*x[j]
            for j in range(i+1, n):
                x[i] -= A[i][j]*x[j]
            x[i] /= A[i][i]
            x[i] = x0 + (x[i] - x0)*w
        margem = b[0]
        for i in range(n):
            margem -= A[0][i]*x[i]
    return x, k


A = [
    [3, -1, -1],
    [1, 3, 1],
    [2, -2, 4]
]

b = [1, 5, 4]

erro = 10**(-16)

w = 0.85

x, k = gauss_seidel(A, b, erro, w)

print("A = ")
for i in A:
    print(i)

print("\nb = ")
print(b, end="\n\n")

print(k, "iterações")
print("\nx = ")
print(x)
