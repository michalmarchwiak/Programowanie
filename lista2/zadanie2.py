from PIL import Image
import sys
"""input: w argumentach podac sciezke pliku, rozmiar miniatury oraz sciezke nowego pliku
output: miniatura zdjecia
program tworzacy miniature zdjecia"""

original_file = sys.argv[1]
thumbnail_size = int(sys.argv[2]), int(sys.argv[3])
output_file = sys.argv[4]


with Image.open(original_file) as im:
    im.thumbnail(thumbnail_size)
    im.save(output_file, "JPEG")
