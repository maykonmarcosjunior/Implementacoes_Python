abcm = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c"]
abcd = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
seletor = [abcm, abcd]
cd = int(input())
while True:
    try:
        m = (input().lower()).split()
        N = len(m)
        for i in range(0, N):
            l = seletor[cd].index(m[i])
            m[i] = seletor[cd][l + 3 - 6*cd]
        print("".join(m))
    except EOFError:
        break
