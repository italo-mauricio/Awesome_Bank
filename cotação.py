import requests
import os








def cotacao():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        dolar_value = response.json()['USD']['low']
        print(f'O valor do dólar é R${dolar_value}')
    else:
        print("Erro ao buscar o valor do dólar")