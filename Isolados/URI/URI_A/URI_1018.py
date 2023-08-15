# -*- coding: utf-8 -*-

notas = [100, 50, 20, 10, 5, 2, 1]
saida = input()
valor = int(saida)
for i in notas:
    resto = valor//i
    valor %= i
    saida += ("%d nota(s) de R$ %d,00\n" % (resto, i))
print(saida)
