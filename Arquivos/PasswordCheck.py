import random
import pwinput



def passw(password):
    # uma lista com vários caracteres
    senha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t','u',
            'v', 'x', 'y', 'z', '1','2','3','4','5','6','7','8',
            '9','0','A', 'B', 'C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','@', '_']

    # define password como vazio
    password = ""

    # percorre com um for a quantidade de caracteres que eu quero, no caso é 10
    for x in range(10):
        password = password + random.choices(senha)[0] # passowrd recebe escolhas random
        
    print(f'Sua nova senha é: {password} ') # gera a nova senha
    
    return password
