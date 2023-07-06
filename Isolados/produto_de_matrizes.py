def produbool(a, b, c, d):
    resultado = 0
    N = len(a[b])
    for i in range(N):
        resultado = resultado or (a[b][i] and c[d][i])
    return resultado
def produlc(a, b, c, d):
    resultado = 0
    N = len(a[b])
    for i in range(N):
        resultado += a[b][i] * c[d][i]
    return resultado

operacao = input()
n, m = (int(i) for i in input().split())
mat1 = [None]*n
for i in range(n):
    mat1[i] = (int(j) for j in input().split())
mat2 = [None]*m
for i in range(m):
    mat2[i] = (int(j) for j in input().split())
for g in range(n):
    for h in range(n):
        if operacao == "bool":
            print(produbool(mat1, g, mat2, h), end=' ')
        else:
            print(produlc(mat1, g, mat2, h), end=' ')
    print()
