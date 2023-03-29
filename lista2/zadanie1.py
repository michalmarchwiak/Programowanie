from string import ascii_letters, digits, punctuation
from random import randrange
zasoby=[]
for i in range(len(digits)):
    zasoby.append(digits[i])
for i in range(len(punctuation)):
    zasoby.append(punctuation[i])
for i in range(len(ascii_letters)):
    zasoby.append(ascii_letters[i])

def haslo1(x):
    """input: dlugosc hasla
    output: haslo w stringu
    funkcja generująca hasło złożone z malych liter, wielkich liter, cyfr oraz znaków specjalnych"""
    haslo1=[]
    for i in range(x):
        haslo1.append(zasoby[randrange(0,94,1)])
    return ''.join(haslo1)

print(haslo1(int(input("Długość hasła:"))))

