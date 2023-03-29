import os
from PyPDF2 import PdfReader, PdfWriter


def split_pdf(file_path, page_count, new_file_path):
    """ input: ścieżka pliku, liczba stron w pliku, ścieżka nowych plikóq
        output: brak
        funkcja dzieląca plik pdf na mniejsze pliki z określoną liczbą stron """
    with open(file_path, 'rb') as f:
        pdf = PdfReader(f)
        total_pages = len(pdf.pages)
        page_number = 1
        page_number2 = 10

        for i in range(0, total_pages, page_count):
            output_pdf = PdfWriter()

            for j in range(i, i + page_count):
                if j < total_pages:
                        page = pdf.pages[j]
                        output_pdf.add_page(page)

                else:
                    break
            if len(output_pdf.pages) % 10 != 0:
                page_number2 = total_pages
            output_file_name = os.path.splitext(os.path.basename(file_path))[0] + f'_{page_number}-{page_number2}.pdf'
            output_file_path = os.path.join(new_file_path, output_file_name)
            with open(output_file_path, 'wb') as out_file:
                output_pdf.write(out_file)

            page_number += 10
            page_number2 += 10


file_path = r'C:\Users\Michał\Desktop\Apollo.pdf'
page_count = 10
new_file_path = r'C:\Users\Michał\Desktop\wdp'
split_pdf(file_path, page_count, new_file_path)
