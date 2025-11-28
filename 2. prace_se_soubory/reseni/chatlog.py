cesta = "chatlog.txt"

with open(cesta, "w", encoding="utf-8") as file:
    file.close()

konec = "KONEC"
zprava = ""

print(f"Chatlog opustíš pomocí řetězce \"{konec}\"")

while zprava != konec:
    jmeno = input("Zadej uživatelské jméno: ")
    zprava = input("Zadej svou zprávu: ")

    if zprava != konec:
        with open(cesta, "a", encoding="utf-8") as file:
            file.write(f"{jmeno} - {zprava}\n")
            print("Zprava byla zapsána do souboru \n")
