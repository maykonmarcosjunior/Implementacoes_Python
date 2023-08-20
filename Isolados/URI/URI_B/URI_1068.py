saida = ""
while True:
    try:
        eq = input()
        stack = 0
        for char in eq:
            if char == "(":
                stack += 1
            elif char == ")":
                stack -= 1
            # se um fecha parênteses
            # vier antes do abre
            if stack < 0:
                break
        # se nem todos foram fechados
        if stack:
            saida += "incorrect\n"
        else:
            saida += "correct\n"
    except EOFError:
        break
print(saida, end='')
