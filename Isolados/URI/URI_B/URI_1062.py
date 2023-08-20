saida = ""
while True:
    Nvagoes = int(input())  # Número de vagões

    if not Nvagoes:
        break  # Fim da entrada

    while True:
        perm = input()
        if perm == "0":
            saida += "\n"
            break
        b_order = [int(i) for i in perm.split()]

        stack = []
        a_order = 1

        for wagon in b_order:
            while a_order <= Nvagoes and (not stack or stack[-1] != wagon):
                stack.append(a_order)
                a_order += 1

            if stack[-1] == wagon:
                stack.pop()
            else:
                break

        if not stack:
            saida += "Yes\n"
        else:
            saida += "No\n"

print(saida, end='')
