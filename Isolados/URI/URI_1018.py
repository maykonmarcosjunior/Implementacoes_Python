# -*- coding: utf-8 -*-

notas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input())
print(valor)
for i in notas:
    resto = valor//i
    valor -= i*resto
    print("%d nota(s) de R$ %d,00" % (resto, i))
