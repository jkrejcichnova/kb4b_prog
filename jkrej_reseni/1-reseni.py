import random
import keyboard
def hod_minci() -> str:
    #bylo by lepsi vybrat z listu ale jdu podle zadani
    mince = random.randint(0, 1)
    if mince == 0:
        return "panna"
    else:
        return "orel"

def hod_minci_se_sazenim():
    balance = 100
    exit = False
    while not exit:
        print("Máš {} Kč".format(balance))

        sazka: int = 0
        while sazka == 0:
            sazka_try: int = int(input("Kolik si chceš vsadit? "))
            if sazka_try > balance:
                continue
            sazka = sazka_try
        balance -= sazka
        
        tip: str = ""
        while tip == "":
            tip_guess: str = input("Tipni si (panna/orel): ")
            if tip_guess == "panna" or tip_guess == "orel":
                tip = tip_guess
        
        result: str = hod_minci()
        print("Padlo: {}".format(result))
        
        if result == tip:
            balance += 2*sazka
            print("Vyhráváš {} Kč! Stav účtu: {} Kč".format(2*sazka, balance))
        else:
            print("Prohrál jsi {}! Stav účtu: {} Kč".format(sazka, balance))

        if balance == 0:
            print("Game over...")
            return

        continuation = ""
        while continuation == "":
            cont_try = input("Hrát znovu? [a/n]: ")
            if cont_try == "a" or cont_try == "n":
                continuation = cont_try
        if continuation == "n":
            exit = True
        print("\n")

def hod_kostkou():
    pocet_hodu = int(input("Zadej počet kostek: "))
    pocet_sten = int(input("Zadej počet stěn kostky: "))
    hody: list[int] = []
    for i in range(pocet_hodu):
        hody.append(random.randint(0, pocet_sten))
    print("Hody: {}".format(hody))
    soucet = 0
    for hod in hody:
        soucet += hod
    print("Součet: {}".format(soucet))

def vyber_karty():
    pouzite_kombo: list[tuple[int, int]] = []
    barvy: list[str] = ["Srdce", "Piky", "Kříže", "Káry"]
    hodnoty: list[str] = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Janek", "Král", "Královna", "Eso"]
    done = False
    print("Stiskni cokoliv.")
    while not done:
        keyboard.read_event()
        random_card: tuple[int, int] = ()
        while random_card == ():
            random_card_attempt = (random.randint(0, len(barvy)-1), random.randint(0, len(hodnoty)-1))
            if random_card_attempt not in pouzite_kombo:
                random_card = random_card_attempt
                pouzite_kombo.append(random_card)
        print(barvy[random_card[0]])    
        print("Vytáhl jsi {} - {}".format(barvy[random_card[0]], hodnoty[random_card[1]]))


    

vyber_karty()

    