from datetime import datetime
from textwrap import wrap
def delitele(number: int):
    for i in range(1, number+1):
        if number % i == 0:
            print(i)

def schody(vyska: int, znak: str):
    for i in range(1, vyska+1):
        print(znak*i)

def validator_rcisla(rcislo: str) -> str:
    error_message = "Cislo je neplatne"
    rinfo_raw: list[str] = rcislo.split("/")
    # dve casti
    if len(rinfo_raw) != 2:
        return error_message+": Ma vic jak dve casti"
    
    if len(rinfo_raw[0]) != 6 or not rinfo_raw[0].isdigit():
        return error_message+": Prvni cast neni validni"

    if len(rinfo_raw[1]) != 4 or not rinfo_raw[1].isdigit():
        return error_message+": Druha cast neni validni"
    
    #dob
    dob = rinfo_raw[0]
    dob = wrap(dob, 2)
    byear: int = 0
    if int(dob[0]) <= int(datetime.today().strftime("%y")):
        byear = 2000 + int(dob[0])
    else:
        byear = 1900 + int(dob[0])
    bmonth: int = int(dob[1])
    sex: str = "M"
    if bmonth > 50:
        bmonth = bmonth - 50
        sex = "F"
    bday: int = int(dob[2])

    answer = "Valid Birth certificate number.\nBirthday: {}-{:02d}-{:02d}\nAssigned sex at birth: {}\nCheck number: {}".format(byear,bmonth,bday,sex,rinfo_raw[1])
    return answer

def validator_vstupu() -> int:
    while True:
        user_input = input("Zadejte libovolne kladne trimistne sude cislo: ")
        possible_answer: int = 0
        try:
            possible_answer = int(user_input)
        except ValueError:
            print("Musite zadat cislo")
            continue
        if possible_answer < 100 or possible_answer > 999:
            print("Cislo musi byt kladne a trimistne")
            continue
        if (possible_answer % 2) == 1:
            print("Cislo musi byt sude")
            continue
        return possible_answer
    
def vymazani_duplicit(og_list: list) -> list:
    seen_items: list = []
    for i in range(0, len(og_list)):
        if og_list[i] not in seen_items:
            seen_items.append(og_list[i])            
    return seen_items
        
def validace_emailu(email: str) -> bool:
    try:
        email_list: list = email.split('@')
        if len(email_list) > 2:
            return False
        local_name: str = email_list[0]
        domain: list[str] = email_list[1].split('.')
        if len(domain) > 2:
            return False
        if not local_name.isalnum() or not domain[0].isalnum() or not domain[1].isalpha():
            print(local_name)
            return False
    except:
        return False
    return True

print(validace_emailu("j@nkrej.ci"))