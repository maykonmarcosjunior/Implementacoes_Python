n = int(input())
countries = []

for _ in range(n):
    name, gold, silver, bronze = input().split()
    countries.append((name, int(gold), int(silver), int(bronze)))

countries.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))

for country in countries:
    name, gold, silver, bronze = country
    print(f"{name} {gold} {silver} {bronze}")
