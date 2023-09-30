import random


def passw(password):
    senha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t','u',
            'v', 'x', 'y', 'z', '1','2','3','4','5','6','7','8',
            '9','0','A', 'B', 'C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','@', '_']

    password = ""

    for x in range(10):
        password = password + random.choices(senha)[0] 
        
    print(f'Your new Password: {password}')
    
    return password
