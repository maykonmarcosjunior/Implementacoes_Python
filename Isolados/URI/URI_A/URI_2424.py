# -*- coding: utf-8 -*-

limite_x = 432
limite_y = 468
saida = ["fora", "dentro"]

x, y = [int(i) for i in input().split()]
c1 = x >= 0 and x <= limite_x
c1 = c1 and y >= 0 and y <= limite_y
print(saida[int(c1)])
