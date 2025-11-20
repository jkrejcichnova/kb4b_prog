# Ukazka "w" (write)
# Pokud soubor neexistuje → vytvoří se.
# Pokud existuje → je smazán a vytvoří se nový
with open("zapis.txt", "w", encoding="utf-8") as file:
    file.write("Crazy?\n")
    file.write("I was crazy once.\n")

# Ukazka "a" (append)
# Pokud soubor neexistuje → vytvoří se.
# Pokud existuje → zapíše se na konec
with open("zapis.txt", "a", encoding="utf-8") as file:
    file.write("They locked me in a room.\n")
    file.write("A ruber room.\n")

