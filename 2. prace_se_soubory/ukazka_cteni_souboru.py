cesta = "data/slova.txt"

# with open() as file
# Otevření souboru v režimu pro čtení "r" s UTF-8 kódováním
with open(cesta, "r", encoding="utf-8") as file:
    for line in file:
        slovo = line.strip()    # funcke slip slouží k odstranění bílých znaků na začátku/konci
        print(slovo)

print("\n\n")


# .split()
# Může se také hodit funkce split, která dokáže rozdělit delší string na pole stringů dle mezer:
veta = "I know he ***** swapped those numbers!"
slova = veta.split()
print(slova)

# .split() může mít i jiný dělící znak než mezeru:
text = "Máma mele maso. Ola solí. Máma má mísu."
jednotlive_vety = text.split(".")
print(jednotlive_vety)
