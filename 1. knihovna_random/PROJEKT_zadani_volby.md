# Úloha – Simulace voleb do Poslanecké sněmovny 2025 (Python)

Vytvoř program v jazyce **Python 3**, který simuluje volby do Poslanecké sněmovny 2025.

Při řešení programu ber v potaz:
- čitelnost
- modularitu (místo jednoho velkého bloku kódu využívej pomocné funkce)
- možnost změn a budoucích rozšíření

---

## Zadání

1. **Seznam politických stran**
   - Měj list s názvy alespoň 6 stran, např.:
     ```python
     strany = ["ANO", "SPOLU", "SPD", "STAN", "Piráti", "Motoristé", "Stačilo", "Jiné"]
     ```

2. **Seznam preferencí (v procentech)**
   - Ulož preferenční váhy ke stejnému pořadí stran:
     ```python
     preference = [29.3, 20.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2]  # data ze STEM 28.9.
     ```
   - *(bonus)* Přidej šum: ke každé preferenci přičti náhodnou odchylku v intervalu ±2%.
     - Dohlédni, aby žádná preference nebyla záporná a aby bylo zachováno 100%.

3. **Účast voličů**
   - Vygeneruj náhodnou volební účast (float) v rozsahu **50–80 %**.
   - Zvol si celkový počet oprávněných voličů a z toho dopočti počet hlasujících.

4. **Simulace hlasování**
   - Pro každého voliče náhodně vyber stranu **podle vahy** `preference`.
        - např. šance volby ANO je 29.3%, šance volit SPOLU je 20.5%, ...
   - Spočítej počet hlasů pro každou stranu.

5. **Výstup programu**
   - Pro každou stranu vypiš:
     - celkový **počet hlasů**,
     - **procentuální zisk** (zaokrouhli na 2 desetinná místa),
     - informaci, zda překročila **5% hranici** pro vstup do sněmovny.
   - Urči **stranu s největším počtem hlasů**.

6. **Textový histogram výsledků**
   - vypiš výsledky pomocí grafu, kde 1 hvězdička `*` = **1 %** hlasů 
   - Vzor formátování:
```
ANO:        32.5 %  ********************************
SPOLU:      21.3 %  *********************
SPD:        10.7 %  **********
STAN:        8.4 %  ********
Piráti:      7.8 %  *******
Motoristé:   5.6 %  *****
Stačilo:     4.1 %  ****
Jiné:        9.6 %  *********
```

7. **Přepočet na mandáty**
   - Přepočítáváš 200 křesen pro strany nad 5 %

---

## Možná rozšíření (specifická pro Python):
- Vykresli výsledky pomocí grafu knihovny matplotlib
- Vypiš všechny možnosti **volebních koalic** – všechny minumální množiny stran, které dohromady získají většinu.
- Umožni porovnání více simulací (např. 100 běhů) a spočítej průměrné výsledky.
