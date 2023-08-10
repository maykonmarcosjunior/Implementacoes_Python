# -*- coding: utf-8 -*-

Npedras, Nsapos = input().split()
Npedras, Nsapos = int(Npedras), int(Nsapos)
saida = [0]*(Npedras + 1)
for i in range(Nsapos):
    pedraI, pulo = input().split()
    pedraI, pulo = int(pedraI), int(pulo)
    saida[pedraI] = 1
    for j in range(pedraI, Npedras+1, pulo):
        saida[j] = 1
    for j in range(pedraI, 0, -pulo):
        saida[j] = 1
for i in range(1, Npedras+1):
    print(saida[i])
