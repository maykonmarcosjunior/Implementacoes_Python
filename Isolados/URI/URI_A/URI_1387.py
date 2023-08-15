# -*- coding: utf-8 -*-

saida = ""
while True:
    e, r = input().split()
    if e == r == '0':
        break
    saida += str(int(e) + int(r))
print(saida)
