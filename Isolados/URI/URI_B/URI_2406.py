def is_well_defined(expression):
    stack = []

    for char in expression:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False

            top = stack.pop()

            if (top == "(" and char != ")") or (top == "[" and char != "]") or (top == "{" and char != "}"):
                return False

    return len(stack) == 0


t = int(input())

for _ in range(t):
    expression = input().strip()
    result = "S" if is_well_defined(expression) else "N"
    print(result)
