# -*- coding: utf-8 -*-
saida = ""
Ncasos = int(input())
for caso in range(Ncasos):
    Nenderecos, Nchaves = (int(i) for i in input().split())
    chaves = input().split()
    tabela = [[str(i)] for i in range(Nenderecos)]
    for i in chaves:
        tabela[int(i) % Nenderecos].append(i)
    if caso:
        saida += "\n"
    for i in tabela:
        for j in i:
            saida += (j + " -> ")
        saida += "\\\n"
print(saida, end='')
