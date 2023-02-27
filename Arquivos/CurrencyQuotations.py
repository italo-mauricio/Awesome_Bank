import requests
import os
from datetime import datetime
from datetime import date
from Screens import *



# Cotação do Dólar Americano

def dolar():
    clean_window()
    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'  # Url para verificar em tempo real a cotação do Dólar

    response = requests.get(url) # Comando .get para pegar essa URL e adicionar a biblioteca

    if response.status_code == 200:
        dolar_value = float(response.json()['USD']['low']) # Utilizando o float para o cálculo de conversão
        print(f'''
              
            | ============================================================= |
            |                        Awesome Bank                             |
            \                                                              /
                                                                           
                 The Dóllar value in Brazilian Real is R${dolar_value:.2f}    
            
            /                                                               \ 
            |
            | ------------------------------------------------------------- |
            | ======================== since 2022 ========================= |
              
              ''')
        while True:
            convert = input("Do you want to convert your currency to dollar: [Y/N] ").strip().lower()
            if convert == 'Y':
                real = float(input("Enter how much you want to convert real R$: "))
                conv = real / dolar_value
                print(f"Their R${real} converted stay USD$ {conv:.2f}")
                conti = input(("Press START for continue..."))
                break
            elif convert == 'N':
                print("Thank you!")
                break
            
            else:
                print("Choose a valid option!")
    else:
        print("Error fetching dollar value") 
         
               
         
         
# Cotação do Euro         
         
def euro():
    clean_window()
    url = 'https://economia.awesomeapi.com.br/all/EUR-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        euro_value = float(response.json()['EUR']['low'])
        print(f'''
              
            | ============================================================= |
            |                        Awesome Bank                           |
            \                                                              /
                                                                           
                   The Euro value in Brazilian Real is R${euro_value:.2f}    
            
            /                                                               \ 
            |
            | ------------------------------------------------------------- |
            | ======================== since 2022 ========================= |
              
              ''')
        while True:
            convert_coin = input("Do you want to convert your currency to Euro: [Y/N] ").strip().lower()
            if convert_coin == 'Y'.strip():
                real = float(input("Enter how much you want to convert real R$: "))
                convert_real = real / euro_value
                print(f"Their R${real} converted stay EUR${convert_real:.2f}")
                input(("Press START for continue..."))
                break
                 
            if convert_coin == 'N'.strip():
                print("Thank You!")
                break
            
            else:
                print("Choose a valid option!")
                
    else:
        print("Error fetching euro value!")
    
    
    
# Cotação do Bitcoin    
        
def bitcoin():
    clean_window()
    url = 'https://economia.awesomeapi.com.br/all/BTC-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        bitcoin_value = float(response.json()['BTC']['low'])
        print(f'''
              
            | ============================================================= |
            |                        Awesome Bank                           |
            \                                                              /
                                                                           
                The BItcoin value in Brazilian Real is R${bitcoin_value:.3f}    
            
            /                                                               \ 
            |
            | ------------------------------------------------------------- |
            | ======================== since 2022 ========================= |
              
              ''')
        while True:
            convert_coin = input("Do you want to convert your currency to Bitcoin: [Y/N] ").strip().lower()
            if convert_coin == 'Y':
                real = float(input("Enter how much you want to convert real R$: "))
                convert_real = real / bitcoin_value
                print(f"Their R${real} converted stay BTC$: {convert_real:.2f}")
                input(("Press START for continue..."))
                break
                 
            if convert_coin == 'N':
                print("Thank You!")
                break
            
            
            else:
                print("Choose your a option!")
        
    else:
        print("Error fetching bitcoin value!")
        
       
# Cotação do Franco       
        
def franco():
    clean_window()
    url = 'https://economia.awesomeapi.com.br/all/CHF-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        franco_value = float(response.json()['CHF']['low'])
        print(f'''
              
            | ============================================================= |
            |                        Awesome Bank                           |
            \                                                              /
                                                                           
               The Franco value in Brazilian Real is R${franco_value:.2f}    
            
            /                                                               \ 
            |
            | ------------------------------------------------------------- |
            | ======================== since 2022 ========================= |
              
              ''')
        while True:
            convert_coin = input("Do you want to convert your currency to Franco: [Y/N] ").strip().lower()
            if convert_coin == 'Y':
                real = float(input("Enter how much you want to convert real R$: "))
                convert_real = real / franco_value
                print(f"Their R${real} converted stay CHF$: {convert_real:.2f}")
                input(("Press START for continue..."))
                break
                 
            if convert_coin == 'N'.lower():
                print("Thank You!")
                break        
            else:
                print("Choose your a option!")
        
    else:
        print("Error fetching bitcoin value!")
        
        
       
# Cotação do Iene 
        
def iene():
    clean_window()
    url = 'https://economia.awesomeapi.com.br/all/JPY-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        iene_value = float(response.json()['JPY']['low'])
        print(f'''
              
            | ============================================================= |
            |                         Awesome Bank                          |
            \                                                              /
                                                                           
                    The Iene value in Brazilian Real is R${iene_value:.2f}    
            
            /                                                               \ 
            |
            | ------------------------------------------------------------- |
            | ======================== since 2022 ========================= |
              
              ''')
        while True:
            convert = input("Do you want to convert your currency to Iene: [Y/N] ").strip().lower()
            if convert == 'Y'.lower():
                real = float(input("Enter how much you want to convert real R$: "))
                conv = real / iene_value
                print(f"Their R${real} converted stay JPY$: {conv:.2f}")
                conti = input(("Press START for continue..."))
                break
                 
            if convert == 'N'.lower():
                print("Thank You!")
                break
            
            
            else:
                print("Choose your a option!")
        
    else:
        print("Error fetching Iene value!")
        
        
        
# Cotação do Dólar Canadense        
        
def dolarcanadense():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/CAD-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        cad_value = float(response.json()['CAD']['low'])
        print(f'''
              
            | ============================================================= |
            |                        Awesome Bank                           |
            \                                                              /
                                                                           
                    The Franco value in Brazilian Real is R${cad_value:.2f}    
            
            /                                                               \ 
            |
            | ------------------------------------------------------------- |
            | ======================== since 2022 ========================= |
              
              ''')
        while True:
            convert = input("Do you want to convert your currency to Canadian dollar: [Y/N] ").strip().lower()
            if convert == 'Y'.lower():
                real = float(input("Enter how much you want to convert real R$: "))
                conv = real / cad_value
                print(f"Their R${real} converted stay CAD$: {conv:.2f}")
                conti = input(("Press START for continue..."))
                break
                 
            if convert == 'N'.lower():
                print("Thank You!")
                break
            
            
            else:
                print("Choose your a option!")
        
    else:
        print("Error fetching Iene value!")
        
        
        
# Menu principal        
        
def menu_cotation():
    while True:
        clean_window()
        print(f'''
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

        option = ' '
        option = input("Choose your option: ")
        if option == '1':
            dolar()
        elif option == '2':
            euro()
        elif option == '3':
            franco()
        elif option == '4':
            bitcoin()
        elif option == '5':
            iene()
        elif option == '6':
            dolarcanadense()
        elif option == '0':
            clean_window()
            break
        else:
            print("Invalid Option")






def __init__(self):
    menu_cotation()