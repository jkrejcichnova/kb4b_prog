from numpy import random
random.seed()
#pre-election info

strany = ["ANO", "SPOLU", "SPD", "STAN", "Piráti", "Motoristé", "Stačilo", "Jiné"]
preference_pruzkum = [29.3, 20.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2]
pocet_opravnenych: int = random.randint(8_000_000, 9_000_000)

#election info

def list_int_to_percentage(l: list[float]) ->list[float]:
    list_percentage: list[float] = []
    for i in l:
        list_percentage.append(i/100)
    return list_percentage

def pridani_sumu(l: list[float]) -> list[float]:
    result = [0]*len(l)
    size_sample = 1000
    distorted_chances = random.choice(range(0,len(l)), p=l, size=size_sample)
    for i in distorted_chances:
        result[i] += 100/size_sample
    return list_int_to_percentage(result)

volebni_ucast: float = random.uniform(0.5, 0.8)
volebni_sance = pridani_sumu(list_int_to_percentage(preference_pruzkum))
pocet_volicu: int = int(volebni_ucast*pocet_opravnenych)
volby = random.choice(strany, p=volebni_sance, size=pocet_volicu)

#post-election info

def election_to_results(election: list[str]) -> dict[str,int]:
    result: dict[str,int] = {}
    for strana in strany:
        result[strana] = 0
    for volba in volby:
        result[volba] += 1
    return result

results = election_to_results(volby)

def print_results(results:dict[str,int]):
    sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

    for strana, vysledek in results.items():
        pp = ''
        if (vysledek/pocet_volicu*100) > 5:
            pp = '\033[92m'

        print(pp + "{0:<16} {2:<5}  {1:>.2%}".format(strana,vysledek/pocet_volicu,'*'*int(vysledek/pocet_volicu*100)) + "\033[0m")
    print(sorted_results)
print_results(results)
    



