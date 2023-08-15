# -*- coding: utf-8 -*-
const_limiar = 127
const_A = ord("A")
const_ast = ord("*")
saida = ""
while True:
    questoes = int(input())
    if questoes == 0:
        break
    for _ in range(questoes):
        pergunta = input().split()
        cont = 0
        resp = [0, const_ast]
        opcoes = len(pergunta)
        for i in range(opcoes):
            cond = int(int(pergunta[i]) <= const_limiar)
            cont += cond
            resp[0] += (const_A + i)*cond
        saida += (chr(resp[cont != 1])) + "\n"
print(saida)
