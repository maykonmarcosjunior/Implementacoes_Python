# -*- coding: utf-8 -*-

def encripty_str(string0):
    texto = list(string0)
    L = len(texto)
    meio = L//2
    texto.reverse()
    for i in range(L):
        cond0 = int(texto[i].isalpha())
        cond1 = int(i >= meio)
        texto[i] = chr(ord(texto[i]) + 3*cond0 - cond1)
    return ''.join(texto)


casos = int(input())
saida = ""
for _ in range(casos):
    saida += (encripty_str(input())) + "\n"
print(saida)
