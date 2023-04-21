import os
import shutil
import datetime

# lista katalogów, w których szukamy plików
search_dirs = ["C:\\Users\\Michał\\Desktop"]

# lista rozszerzeń plików, których szukamy
extensions = [".txt", ".pdf", ".jpg", ".png", ".mp3"]

# katalog, do którego będą kopiowane pliki
backup_dir = "D:\\ppl"

# tworzenie nazwy katalogu kopii zapasowej z datą
now = datetime.datetime.now()
backup_date = now.strftime("%Y-%m-%d")
backup_copy_dir = os.path.join(backup_dir, "copy-" + backup_date)

# tworzenie katalogu kopii zapasowej
if not os.path.exists(backup_copy_dir):
    os.makedirs(backup_copy_dir)

# iteracja przez każdy katalog i wyszukiwanie plików o zadanym rozszerzeniu
for search_dir in search_dirs:
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if os.path.splitext(file)[1] in extensions:
                file_path = os.path.join(root, file)
                # sprawdzenie daty ostatniej modyfikacji pliku
                modified_time = os.path.getmtime(file_path)
                modified_date = datetime.datetime.fromtimestamp(modified_time)
                delta_time = now - modified_date
                if delta_time.days <= 3:
                    # tworzenie ścieżki do pliku w katalogu kopii zapasowej
                    backup_file_path = os.path.join(backup_copy_dir, file)
                    # kopiowanie pliku do katalogu kopii zapasowej
                    shutil.copy2(file_path, backup_file_path)

print("Kopie zapasowe plików zmodyfikowanych w ostatnich trzech dniach zostały utworzone w katalogu", backup_copy_dir)
