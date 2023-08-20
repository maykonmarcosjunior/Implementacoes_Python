saida = []
while True:
    Ncartas = int(input())
    if not Ncartas:
        break
    pilha = [i for i in range(Ncartas, 0, -1)]
    descarte = []
    while len(pilha) > 1:
        descarte.append(str(pilha.pop()))
        pilha.insert(0, pilha.pop())
    saida.append("Discarded cards: ")
    saida.append(', '.join(descarte))
    saida.append("\nRemaining card: %d\n" % (pilha[0]))
print("".join(saida), end='')
