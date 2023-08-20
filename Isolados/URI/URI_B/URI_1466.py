class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def print_bfs(root):
    if root is None:
        return
    queue = [root]
    saida = ""
    while queue:
        current = queue.pop(0)
        saida += str(current.value) + " "
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print(saida[:-1], end='\n\n')


num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    values = list(map(int, input().split()))
    root = None
    for value in values:
        root = insert(root, value)
    print(f"Case {case}:")
    print_bfs(root)
