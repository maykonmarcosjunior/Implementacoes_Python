# -*- coding: utf-8 -*-
saida = ""
while True:
    entr = input().split()
    if entr[0] == entr[1] == entr[2] == entr[3] == '0':
        break
    t1 = int(entr[0])*60 + int(entr[1])
    t2 = int(entr[2])*60 + int(entr[3])
    saida += str((t2 - t1) % 1440)
print(saida)
