# -*- coding: utf-8 -*-
import bisect

caso = 1
saida = ""
while True:
    Npecas, Nquestions = (int(i) for i in input().split())
    if Npecas == Nquestions == 0:
        break
    Marbles = []
    for i in range(Npecas):
        N = int(input())
        bisect.insort(Marbles, N)

    saida += ("CASE# %d:\n" % (caso))
    caso += 1
    for i in range(Nquestions):
        quest = int(input())
        if quest in Marbles:
            saida += ("%d fount at %d\n" % (quest, Marbles.index(quest) + 1))
        else:
            saida += ("%d not found\n" % (quest))
print(saida)
