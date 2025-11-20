import random


def generuj_priklad():
    # vystup: bool vyřešil uživatel příklad
    # vygeneruje priklad
    cislo1 = random.randint(0, 10)
    op = random.choice(["+", "-", "*"])
    cislo2 = random.randint(0, 10)

    print(f"{cislo1} {op} {cislo2} = ")
    vstup = int(input())

    if op == "+":
        spravne = cislo1 + cislo2
    elif op == "-":
        spravne = cislo1 - cislo2
    elif op == "*":
        spravne = cislo1 * cislo2

    return vstup == spravne


pocet_prikladu = 3
body = 0
for i in range(pocet_prikladu):
    if generuj_priklad():
        body += 1

print(f"vyřešil jsi {body}/{pocet_prikladu}")
