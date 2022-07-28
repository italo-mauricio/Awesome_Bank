def saque():
    valor = int(input('Qual o valor você quer sacar da sua conta: '))
    cedula = 50
    total = valor
    cedt = 0
    while True:
        if total >= cedula:
            total -= cedula
            cedt +=1
        else:
            print(f'Total de {cedt} céduas de R${cedula}')
            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            cedt = 0
            if total == 0:
                break