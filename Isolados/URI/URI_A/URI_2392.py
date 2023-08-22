# -*- coding: utf-8 -*-
from Isolados.URI.URI_A.URI_1018 import saida

Npedras, Nsapos = [int(i) for i in input().split()]
saida = [""]*(Npedras + 1)
for i in range(Nsapos):
    pedraI, pulo = [int(i) for i in input().split()]
    saida[pedraI] = "1\n"
    for j in range(pedraI, Npedras+1, pulo):
        saida[j] = "1\n"
    for j in range(pedraI, 0, -pulo):
        saida[j] = "1\n"
print("".join(saida), end='')
