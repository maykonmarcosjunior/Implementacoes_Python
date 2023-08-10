# -*- coding: utf-8 -*-
saidas = ["divisa", "SO", "SE", "NO", "NE"]
while True:
    consultas = int(input())
    if consultas == 0:
        break
    n, m = input().split()
    n, m = int(n), int(m)
    for _ in range(consultas):
        coord = input().split()
        x = int(coord[0])
        y = int(coord[1])
        # divisa
        cond0 = (n != x) and (y != m)
        # se é mais ao leste
        cond1 = (x > n)
        # se é mais ao norte
        cond2 = (y > m)
        # hashmap
        indice = (1 + cond1 + 2*cond2)*cond0
        print(saidas[indice])
