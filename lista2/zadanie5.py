from PIL import Image, ImageEnhance
import sys

if len(sys.argv) != 4:
    raise ValueError("Podaj ścieżkę do pliku graficznego oraz ścieżkę do znaku wodnego oraz wartość przezroczystości jako argumenty wywołania skryptu.")

image_path = sys.argv[1]
watermark_path = sys.argv[2]

try:
    # Wczytaj obraz i znak wodny
    image = Image.open(image_path).convert('RGBA')
    watermark = Image.open(watermark_path).convert('RGBA')

    # Dopasuj rozmiar znaku wodnego do rozmiaru obrazu
    width, height = image.size
    watermark = watermark.resize((int(width / 3), int(height / 3)))

    # Pobierz zadany poziom przezroczystości ze zmiennej określonej przez użytkownika
    alpha = float(sys.argv[3])

    # Utwórz maskę przezroczystości na podstawie kanału alpha
    alpha_band = watermark.getchannel('A')
    alpha_mask = ImageEnhance.Brightness(alpha_band).enhance(alpha)

    # Umieść znak wodny na obrazie
    x = int((width - watermark.width) / 2)
    y = int((height - watermark.height) / 2)
    image.paste(watermark, (x, y), alpha_mask)

    # Zapisz obraz z dodanym znakiem wodnym
    image.save("obraz_z_znakiem_wodnym.png")
    print("Znak wodny został dodany do obrazu.")

except IOError:
    print("Nie można wczytać pliku graficznego lub znaku wodnego.")
