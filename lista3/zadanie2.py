import os

# funkcja do zamiany znaków końca linii
def convert_line_endings(file_path, old_line_ending, new_line_ending):
    # odczytanie pliku
    with open(file_path, 'rb') as file:
        content = file.read()

    # zamiana znaków końca linii
    content = content.replace(old_line_ending, new_line_ending)

    # zapisanie zmienionego pliku
    with open(file_path, 'wb') as file:
        file.write(content)


# lista plików, które będą modyfikowane
files_to_modify = ["C:\\Users\\Michał\\Desktop\\talking.txt"]

# pętla po każdym pliku
for file in files_to_modify:
    # odczytanie ścieżki do pliku
    file_path = os.path.abspath(file)

    # odczytanie aktualnego znaku końca linii
    with open(file_path, 'rb') as file:
        content = file.read()
    if b'\r\n' in content:
        old_line_ending = b'\r\n'
        new_line_ending = b'\n'
    elif b'\n' in content:
        old_line_ending = b'\n'
        new_line_ending = b'\r\n'
    else:
        print("Plik", file, "nie jest plikiem tekstowym lub jest pusty.")
        continue

    # zamiana znaków końca linii
    convert_line_endings(file_path, old_line_ending, new_line_ending)

    # wydrukowanie informacji o wykonanej konwersji
    print("Zamieniono znaki końca linii w pliku", file, "z", repr(old_line_ending), "na", repr(new_line_ending))
