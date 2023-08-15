# -*- coding: utf-8 -*-
saidas = ["divisa\n", "SO\n", "SE\n", "NO\n", "NE\n"]
output = ""
while True:
    consultas = int(input())
    if consultas == 0:
        break
    n, m = input().split()
    n, m = int(n), int(m)
    for _ in range(consultas):
        x, y = [int(i) for i in input().split()]
        # divisa
        cond0 = (n != x) and (y != m)
        # se é mais ao leste
        cond1 = (x > n)
        # se é mais ao norte
        cond2 = (y > m)
        # hashmap
        indice = (1 + cond1 + 2*cond2)*cond0
        output += saidas[indice]
print(output, end='')
