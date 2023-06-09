def produbool(a, b, c, d):
    resultado = False
    for i in range(len(a[b])):
        m1 = True
        m2 = True
        if a[b][i] == 0:
            m1 = False
        if c[d][i] == 0:
            m2= False
        resultado = resultado or (m1 and m2)
    if resultado:
        return 1
    else:
        return 0

def produlc(a, b, c, d):
    resultado = 0
    for i in range(len(a[b])):
        resultado += a[b][i] * c[d][i]
    return resultado

operacao = input()
n = int(input())
mat1 = [None]*n
for i in range(n):
    mat1[i] = input().split()
    for j in range(len(mat1[i])):
        mat1[i][j] = int(mat1[i][j])
m = int(input())
mat2 = [None]*m
for i in range(m):
    mat2[i] = [None]*m
for i in range(m):
    v = input().split()
    for j in range(m):
        mat2[j][i] = int(v[j])
for g in range(n):
    for h in range(n):
        if operacao == "bool":
            print(produbool(mat1, g, mat2, h), end=' ')
        else:
            print(produlc(mat1, g, mat2, h), end=' ')
    print()
