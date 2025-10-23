import random


def pocet_volici(min_procento, max_procento, populace):
    ucast = random.uniform(min_procento, max_procento)    
    return round(populace * ucast)


def inicializuj_vysledky(strany):
    vysledky = {}
    for strana in strany:
        vysledky[strana] = 0
    return vysledky


def vypis_vysledky(vysledky, celkove_hlasy):
    #for strana, hlasy in vysledky.items():
    for strana, hlasy in sorted(vysledky.items(), key=lambda p:p[1], reverse=True):
        print(f"{strana}: {hlasy} hlasů - {round((hlasy/celkove_hlasy)*100, 2)}%")


# definovani stran a preferenci
strany = ["ANO", "SPOLU", "SPD", "STAN", "Piráti", "Motoristé", "Stačilo", "Jiné"]
preference = [29.3, 20.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2]  # data ze STEM 28.9.
populace = 1000

# generovani poctu volici
volici = pocet_volici(50, 80, populace)

# generovani hlasu
vysledky = inicializuj_vysledky(strany)

for _ in range(volici):
    hlas = random.choices(strany,  weights=preference)[0]
    vysledky[hlas] += 1

# vypsani vysledku
vypis_vysledky(vysledky, volici)
    