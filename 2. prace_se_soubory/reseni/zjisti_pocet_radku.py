cesta = "2. prace_se_soubory\data\studenti.txt"

with open(cesta, "r", encoding="utf-8") as soubor:

    text = soubor.read()
    delka = 0

    for line in text.split():
        print(line)
        delka += 1

    print("Pocet radku souboru je", delka)
