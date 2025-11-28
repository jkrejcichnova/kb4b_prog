def generuj_priklad(radek):
    # vystup: bool vyřešil uživatel příklad
    # vygeneruje priklad
    cislo1 = int(radek.split()[0])
    op = radek.split()[1]
    cislo2 = int(radek.split()[2])

    print(f"{cislo1} {op} {cislo2} = ")
    vstup = int(input())

    if op == "+":
        spravne = cislo1 + cislo2
    elif op == "-":
        spravne = cislo1 - cislo2
    elif op == "*":
        spravne = cislo1 * cislo2

    return vstup == spravne


cesta = "2. prace_se_soubory\data\priklady.txt"
with open(cesta, "r", encoding="utf-8") as file:
    radky = file.readlines()
    
    pocet_prikladu = 3
    body = 0
    for i in range(pocet_prikladu):
        if generuj_priklad(radky[i].strip()):
            body += 1

    print(f"vyřešil jsi {body}/{pocet_prikladu}")
