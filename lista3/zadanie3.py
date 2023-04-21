import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_dir, output_path):
    # Utwórz obiekt mergera
    merger = PdfMerger()

    # Przejdź przez każdy plik PDF w podanym katalogu wejściowym
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            # Wczytaj plik PDF i dodaj go do mergera
            with open(os.path.join(input_dir, filename), 'rb') as f:
                merger.append(f)

    # Zapisz połączony plik PDF do podanej ścieżki wyjściowej
    with open(output_path, 'wb') as out_file:
        merger.write(out_file)


# Przykładowe użycie
input_dir = 'C:/Users/Michał/Desktop/wdp'
output_path = 'C:/Users/Michał/Desktop/wdp/appollo.pdf'
merge_pdfs(input_dir, output_path)
