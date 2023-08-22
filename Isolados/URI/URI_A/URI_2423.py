# -*- coding: utf-8 -*-
def min(A, B, C):
    cond1 = int(A <= B and A <= C)
    cond2 = int(B <= A and B <= C)
    cond3 = int(C <= A and C <= B)
    saida = [A, B, C]
    indice = (3*cond1 + cond2 + 2*cond3 - (cond2 and cond3)) % 3
    return saida[indice]


entr = input().split()
A = int(entr[0])//2
B = int(entr[1])//3
C = int(entr[2])//5
print(min(A, B, C))
