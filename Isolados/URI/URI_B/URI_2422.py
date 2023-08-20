def find_brinquedos(casas, k):
    left, right = 0, len(casas) - 1

    while left < right:
        current_sum = casas[left] + casas[right]
        if current_sum == k:
            return casas[left], casas[right]
        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return None, None


n = int(input())
casas = [int(input()) for _ in range(n)]
k = int(input())

brinquedo1, brinquedo2 = find_brinquedos(casas, k)

if brinquedo1 is not None and brinquedo2 is not None:
    print(f"{brinquedo1} {brinquedo2}")
