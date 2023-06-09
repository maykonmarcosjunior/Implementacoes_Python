cd = int(input())
abcm = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c"]
abcd = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while True:
    try:
        m = input()
        m = m.lower()
        m = list(m)
        for i in range(0, len(m)):
            if cd == 0:
                l = abcm.index(m[i])
                m[i] = abcm[l+3]
            else:
                l = abcd.index(m[i])
                m[i] = abcd[l-3]
        m = "".join(m)
        print(m)
    except EOFError:
        break
