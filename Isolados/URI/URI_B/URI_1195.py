class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.left = None
        self.right = None

    def insere(self, filho):
        if filho.valor > self.valor:
            if self.right is None:
                self.right = filho
            else:
                self.right.insere(filho)
        else:
            if self.left is None:
                self.left = filho
            else:
                self.left.insere(filho)

    def traverse(self, lista: list, order: str):
        if order == 'Pre.: ':
            lista.append(str(self.valor))
        if self.left is not None:
            self.left.traverse(lista, order)
        if order == 'In..: ':
            lista.append(str(self.valor))
        if self.right is not None:
            self.right.traverse(lista, order)
        if order == 'Post: ':
            lista.append(str(self.valor))
        return lista


saida = []
Ncasos = int(input())
for caso in range(1, Ncasos + 1):
    saida.append("Case %d:\n" % caso)
    Nnodos = int(input())
    nodos = [Nodo(int(i)) for i in input().split()]
    head = nodos[0]
    for i in nodos[1:]:
        head.insere(i)
    orders = ['Pre.: ', 'In..: ', 'Post: ']
    for order in orders:
        traversal = head.traverse([], order)
        saida.append(order + ' '.join(traversal) + "\n")
    saida.append("\n")

print(''.join(saida), end='')
