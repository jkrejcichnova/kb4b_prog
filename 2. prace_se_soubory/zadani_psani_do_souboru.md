# Úlohy - zápis do souboru
Úlohy jsou seřazeny *přibližně* od jednodušších po složitější.

---

## 1) **Generátor náhodných čísel**

Vytvoř program, který bude generovat náhodná čísla a ukládat je do souboru.

1. Uživatel zadá tři hodnoty:
   - minimální hodnotu (např. `1`),
   - maximální hodnotu (např. `100`),
   - kolik čísel chce vygenerovat (např. `20`).
2. Program vygeneruje požadovaný počet náhodných **celých** čísel z daného intervalu.
3. Všechna čísla uloží do souboru. Každé číslo na samostatný řádek.

---

## 2) **Chatlog – souborový chat**

Naprogramuj jednoduchý textový "chat", který ukládá zprávy do souboru `data/chatlog.txt`.

Program by měl fungovat takto:

1. Uživatel zadá **uživatelské jméno** (např. `cichna-smrdi25`).
2. Uživatel zadá **text zprávy**.
3. Program zprávu **přidá na konec souboru** ve formátu například:
   `cichna-smrdi25: Ahoj, cítíte to taky?`
4. Program se ptá opakovaně na další zprávy (a uživatelská jména), dokud uživatel nenapíše speciální příkaz (např. `konec`) místo zprávy.

Bonus:
- Přidej k každé zprávě čas odeslání (např. `2025-10-03 14:32:10 - cichna-smrdi25: Ahoj, cítíte to taky?`).

---

## 3) **Přihlašování uživatele do herny**

Vytvoř program, který simuluje jednoduchý systém účtů pro herní aplikaci.  
Účty budou uloženy v textovém souboru.


Uživatel si může vybrat z několika akcí:
### a) Vytvoření účtu
1. Nabídni uživateli možnost **vytvořit nový účet**.
2. Uživatel zadá:
   - login (uživatelské jméno),
   - heslo.
3. Program novému účtu nastaví počáteční zůstatek na 1000 Kč.
4. Tyto údaje (login, heslo, zůstatek) zapíšeš do souboru, např. ve formátu:
   `login;heslo;zustatek`

### b) Přihlášení uživatele
1. Uživatel zadá login a heslo.
2. Program zkontroluje v souboru, jestli existuje účet se stejným loginem a heslem.
3. Pokud přihlášení **neuspěje**, vypiš chybovou hlášku.
4. Pokud přihlášení **uspěje**, vypiš aktuální zůstatek uživatele.

### c) Herní část – sázení na hod mincí
1. Po úspěšném přihlášení nabídni uživateli jednoduchou hru (např. sázení se na hod mincí).
2. Pokud hráč vyhraje, přidej mu peníze. Pokud prohraje, odeber mu peníze.
3. Aktualizuj zůstatek v souboru pro daný účet.

Bonus:
- Zabraň vytvoření účtu se stejným loginem, který už v souboru existuje.

---

## 4) **Hromadná změna slov v souboru**

Vytvoř program, který umí nahradit všechna výskyty určitého slova v textovém souboru jiným slovem (ve stylu "najdi a nahraď").

1. Načti libovolný delší textový soubor, např. `1984.txt`.
2. Od uživatele načti dvě slova:
   - **původní slovo** (např. `newspeak`),
   - **nové slovo** (např. `novomluva`).
3. Program:
   - načte obsah souboru,
   - nahradívšechny výskyty původního slova slovem novým,
   - výsledek zapíše do nového souboru.

---

## 5) **To-Do list v souboru**

Vytvoř program, který spravuje jednoduchý To-Do list.

Každý řádek souboru představuje jeden úkol.

Program by měl umět tyto akce:

1. Přidat úkol
2. Vypsat všechny úkoly
3. Smazat úkol
4. Označit úkol jako hotový

---

## 6) **Generátor sudoku zadání do textového souboru**

Vytvoř program, který vygeneruje zadání Sudoku a uloží jej do textového souboru.

Např.:
```
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```

