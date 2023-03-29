def generuj_slupek(dzialanie):
    # Sprawdź, czy to dodawanie, odejmowanie czy mnożenie
    if "+" in dzialanie:
        operator = "+"
        liczby = dzialanie.split("+")
    elif "-" in dzialanie:
        operator = "-"
        liczby = dzialanie.split("-")
    elif "*" in dzialanie:
        operator = "*"
        liczby = dzialanie.split("*")
    else:
        return "Błędne działanie"
    # Usuń spacje
    liczby = [l.strip() for l in liczby]
    # Oblicz wynik
    wynik = eval(dzialanie)
    # Oblicz długość najdłuższego składnika
    dlugosc = max([len(str(l)) for l in liczby] + [len(str(wynik))])
    # Wygeneruj słupek
    slupek = []
    ostatni_skladnik_dodany = False
    for l in liczby:
        if not ostatni_skladnik_dodany:
            if l == liczby[-1]:
                slupek.append(operator + " " * 20 + l.rjust(dlugosc-1))
                ostatni_skladnik_dodany = True
            else:
                slupek.append(" " * 20 + l.rjust(dlugosc))
        else:
            slupek.append(" " * 20 + l.rjust(dlugosc))
    slupek.append(" " * 20 + "-" * dlugosc)
    slupek.append(" " * 20 + str(wynik).rjust(dlugosc))
    return "\n".join(slupek)

print(generuj_slupek("22*2+8"))