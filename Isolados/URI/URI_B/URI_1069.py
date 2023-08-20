saida = ''
Ntestes = int(input())
for _ in range(Ntestes):
    teste = input()
    diamantes = 0
    stack = 0
    for i in teste:
        if i == "<":
            stack += 1
        # se fechar o diamante
        elif i == ">" and stack:
            stack -= 1
            diamantes += 1
    print(diamantes)
