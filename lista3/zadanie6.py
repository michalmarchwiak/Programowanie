import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    # pobieramy losowy artykuł z Wikipedii
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(response.content, "html.parser")

    # wyświetlamy tytuł artykułu
    title = soup.find("title").text
    print(f"Tytuł artykułu: {title}")

    # pytamy użytkownika, czy chce przeczytać dalszą część w przeglądarce
    odpowiedz = input("Czy chcesz przeczytać dalszą część artykułu w przeglądarce? (tak/nie) ")

    # jeśli użytkownik wyraził zgodę, otwieramy przeglądarkę z adresem artykułu i przerywamy pętlę
    if odpowiedz.lower() == "tak":
        url = response.url
        webbrowser.open(url)
        break
