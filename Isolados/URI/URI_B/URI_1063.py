saida = ""
while True:
    Nvagoes = int(input())  # Número de vagões

    if not Nvagoes:
        break  # Fim da entrada
    ordem_a = input().split()
    ordem_esperada = input().split()

    stack = []
    ordem_b = []
    for vagao in ordem_a:
        # significa que netrou na estação
        stack.append(vagao)
        saida += "I"
        # se existe algum vagão na estação e esse vagão for o
        # próximo que deveria sair, ele vai para o trilho b
        while stack and stack[-1] == ordem_esperada[len(ordem_b)]:
            # saiu da estação para ir para o trilho b
            ordem_b.append(stack.pop())
            saida += "R"
    # se ainda estiver na estação
    if stack:
        saida += " Impossible\n"
    else:
        saida += "\n"

print(saida, end='')
