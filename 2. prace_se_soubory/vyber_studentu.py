import random

def vyber_studentu(cesta, n):
    with open(cesta, "r", encoding="utf-8") as file:
        studenti = file.readlines()
        
        for i in range(len(studenti)):
            studenti[i] = studenti[i].strip()

        vybrani = []

        while len(vybrani) < n:
            novy_student = random.choice(studenti)
            if novy_student not in vybrani:
                vybrani.append(novy_student)

        vybrani.sort()
        return vybrani


cesta = "2. prace_se_soubory\data\studenti.txt"
vybrani = vyber_studentu(cesta, 5)

vystupni_soubor = r"2. prace_se_soubory\vystup.txt"

with open(vystupni_soubor, "w", encoding="utf-8") as file:
    for s in vybrani:
        file.write(s + "\n")