import zipfile
import os
import datetime
import sys

directories = []
for i in range(len(sys.argv)):
    directories.append(sys.argv[i])

# Tworzenie nazwy archiwum zawierającej aktualną datę jako przedrostek
now = datetime.datetime.now()
archive_name = now.strftime("%Y-%m-%d") + "_backup.zip"

# Otwieranie pliku archiwum
with zipfile.ZipFile(archive_name, 'w') as zip_file:

    # Iteracja przez każdy katalog i dodawanie jego zawartości do archiwum
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path)

print("Kopia bezpieczeństwa została utworzona w pliku", archive_name)
