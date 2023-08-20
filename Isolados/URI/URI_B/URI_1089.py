while True:
    n = int(input())
    if n == 0:
        break
    o = [int(i) for i in input().split()]
    # para criar o efeito
    # de lista circular
    o.append(o[0])
    o.append(o[1])
    picos = 0
    for i in range(1, n+1):
        # se for maior que o anterior e o proximo
        cond0 = o[i] > o[i-1] and o[i] > o[i+1]
        # se for menor que o anterior e o proximo
        cond1 = o[i] < o[i-1] and o[i] < o[i+1]
        # se ambos forem falsos, soma 0
        picos += cond0 or cond1
    print(picos)
