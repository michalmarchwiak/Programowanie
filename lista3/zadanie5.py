def sprawdz_nawiasy(wyrazenie):
    stos = []
    nawiasy_lewe = ['(', '[', '{']
    nawiasy_prawe = [')', ']', '}']
    for znak in wyrazenie:
        if znak in nawiasy_lewe:
            stos.append(znak)
        elif znak in nawiasy_prawe:
            if not stos:
                return False
            poprzedni = stos.pop()
            if nawiasy_lewe.index(poprzedni) != nawiasy_prawe.index(znak):
                return False
    return not stos

wyrazenie = input("Podaj wyrażenie: ")
if sprawdz_nawiasy(wyrazenie):
    print("Nawiasy są poprawnie użyte.")
else:
    print("Nawiasy są niepoprawne.")
