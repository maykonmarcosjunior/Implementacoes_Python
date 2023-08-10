# -*- coding: utf-8 -*-

casos = int(input())
tipos = {"C": 0, "R": 0, "S": 0}
for _ in range(casos):
    experiencia = input().split()
    tipos[experiencia[1]] += int(experiencia[0])
total = tipos["C"] + tipos["R"] + tipos["S"]
print("Total:", total, "cobaias")
print("Total de coelhos:", tipos["C"])
print("Total de ratos:", tipos["R"])
print("Total de sapos:", tipos["S"])
print("Percentual de coelhos: %.2f %%" % (100*tipos["C"]/total))
print("Percentual de ratos: %.2f %%" % (100*tipos["R"]/total))
print("Percentual de sapos: %.2f %%" % (100*tipos["S"]/total))
