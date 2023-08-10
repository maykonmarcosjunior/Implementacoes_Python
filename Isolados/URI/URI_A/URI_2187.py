# -*- coding: utf-8 -*-

notas = {50: 0, 10: 0, 5: 0, 1: 0}
teste = 1
while True:
    valor = int(input())
    if valor == 0:
        break
    print("Teste", teste)
    notas[50] = notas[10] = 0
    notas[5] = notas[1] = 0
    for i in notas.keys():
        notas[i] = valor//i
        valor %= i
    print(notas[50], notas[10], notas[5], notas[1])
    print()
    teste += 1
