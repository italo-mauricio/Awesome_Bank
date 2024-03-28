import requests
from datetime import datetime
from datetime import date
from screens import *
import requests

import os



def clean_window():
    if os.name == 'nt':  
        _ = os.system('cls')
    else: 
        _ = os.system('clear')


def get_currency_value(currency_code):
    url = f'https://economia.awesomeapi.com.br/all/{currency_code}-BRL'
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()[currency_code]['low'])
    else:
        return None

def convert_currency(currency_name, currency_code):
    clean_window()
    currency_value = get_currency_value(currency_code)

    if currency_value is not None:
        print(f'''
              
            | ============================================================= |
            |                        Awesome Bank                             |
            \                                                              /
                                                                           
               The {currency_name} value in Brazilian Real is R${currency_value:.2f}    
            
            /                                                               \ 
            |
            | ------------------------------------------------------------- |
            | ======================== since 2022 ========================= |
              
              ''')
        while True:
            convert = input(f"Do you want to convert your currency to {currency_name}: [Y/N] ").strip().lower()
            if convert == 'y':
                real = float(input("Enter how much you want to convert real R$: "))
                conv = real / currency_value
                print(f"Their R${real} converted stay {currency_code}: {conv:.2f}")
                conti = input(("Press START for continue..."))
                break
            elif convert == 'n':
                print("Thank You!")
                clean_window()
                break
            else:
                print("Choose your option!")
    else:
        print(f"Error fetching {currency_name} value!")

def menu_cotation():
    while True:
        clean_window()
        print('''
        | ===================== Menu Quotes ==================== |
        | ------------------------------------------------------ |
        | -                 Consult   Dólar    1               - |
        | -                 Consult   Euro     2               - | 
        | -                 Consult   Franco   3               - |
        | -                 Consult   Bitcoin  4               - |
        | -                 Consult   Iene     5               - |
        | -                 Consult   CAD      6               - |
        | -                 Back to main menu  0               - |
        | ------------------------------------------------------ |
        | ====================================================== |
        ''')

        option = input("Choose your option: ").strip()
        if option == '1':
            convert_currency("Dólar", "USD")
        elif option == '2':
            convert_currency("Euro", "EUR")
        elif option == '3':
            convert_currency("Franco", "CHF")
        elif option == '4':
            convert_currency("Bitcoin", "BTC")
        elif option == '5':
            convert_currency("Iene", "JPY")
        elif option == '6':
            convert_currency("CAD", "CAD")
        elif option == '0':
            clean_window()
            break
        else:
            print("Invalid Option")

if __name__ == "__main__":
    menu_cotation()
