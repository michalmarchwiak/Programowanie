import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import os


def get_exchange_rates():
    url = 'http://api.nbp.pl/api/exchangerates/tables/a/'
    response = requests.get(url)
    data = response.json()
    rates = data[0]['rates']
    rates.append({'currency': 'złoty', 'code': 'PLN', 'mid': 1.0})  # Dodanie waluty PLN

    # Zapisanie danych do pliku
    with open('exchange_rates.pickle', 'wb') as file:
        pickle.dump(rates, file)

    return rates


def load_exchange_rates():
    # Sprawdzenie czy plik z danymi istnieje
    if os.path.exists('exchange_rates.pickle'):
        # Odczytanie danych z pliku
        with open('exchange_rates.pickle', 'rb') as file:
            rates = pickle.load(file)
            return rates
    else:
        return None


# Przeliczanie walut
def convert_currency():
    amount = float(entry_amount.get())
    currency_from = combobox_from.get()
    currency_to = combobox_to.get()

    rates = get_exchange_rates() if is_internet_available() else load_exchange_rates()

    if rates is None:
        messagebox.showwarning("Błąd", "Brak dostępnych danych kursów walut.\nSprawdź połączenie z internetem.")
        return

    rate_from = next((rate['mid'] for rate in rates if rate['code'] == currency_from), None)
    rate_to = next((rate['mid'] for rate in rates if rate['code'] == currency_to), None)

    if rate_from and rate_to:
        converted_amount = amount * rate_from / rate_to
        label_result['text'] = f'{converted_amount:.2f} {currency_to}'
    else:
        label_result['text'] = 'Nieznana waluta'


# Funkcja sprawdzająca dostępność połączenia z internetem
def is_internet_available():
    try:
        requests.get('http://api.nbp.pl', timeout=3)
        return True
    except requests.ConnectionError:
        return False


# Funkcja do zamykania kalkulatora
def close_calculator():
    if messagebox.askokcancel("Zamykanie", "Czy na pewno chcesz zamknąć kalkulator?"):
        window.destroy()


# Tworzenie interfejsu graficznego
window = tk.Tk()
window.title('Przelicznik walut')

label_amount = tk.Label(window, text='Kwota:')
label_amount.pack()

entry_amount = tk.Entry(window)
entry_amount.pack()

label_from = tk.Label(window, text='Z:')
label_from.pack()

combobox_from = tk.ttk.Combobox(window)
combobox_from.pack()

label_to = tk.Label(window, text='Na:')
label_to.pack()

combobox_to = tk.ttk.Combobox(window)
combobox_to.pack()

button_convert = tk.Button(window, text='Przelicz', command=convert_currency)
button_convert.pack()

label_result = tk.Label(window, text='')
label_result.pack()

button_close = tk.Button(window, text='Zamknij', command=close_calculator)
button_close.pack()

# Pobranie dostępnych walut i ustawienie ich w comboboxach
rates = get_exchange_rates() if is_internet_available() else load_exchange_rates()

if rates is None:
    messagebox.showwarning("Błąd", "Brak dostępnych danych kursów walut.\nSprawdź połączenie z internetem.")
    window.destroy()
else:
    available_currencies = [rate['code'] for rate in rates]
    combobox_from['values'] = available_currencies
    combobox_to['values'] = available_currencies

window.mainloop()
