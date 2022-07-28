#Essa função serve para validar o CPF do cliente.
def cadastrocpf(cpf):
    # fLAVIUS, RETIRAMOS ESSA VALIDAÇÃO DA INTERNET, NÃO CONSEGUI ACHAR O LINK
    # NÃO CONSEGUIMOS DESENVOLVER O VALIDADOR DE CPF
    #validação do CPF do cliente
    cpf = [int(caracter) for caracter in cpf if caracter.isdigit()]
 
    if len(cpf) != 11: #faz a verificação se o CPF do cliente tem mesmo 11 dígitos
        return False
    
    if cpf == cpf [::-1]: #verifica se tem todos os números iguais, pois mesmos com os números sendo considerados inválidos, eles passam na verificação
        return False

    for i in range(9, 11): #valida os dois dígitos verificadores
        valores = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digito = ((valores * 10) % 11) % 10
        if digito != cpf[i]:
            return False
    return True


def validemail(email): # Validação de Email
    
    tamanho = len(email) #aqui ele faz a contagem da lista de email
    caracteres = ['@', '_', '.'] # decidimos levar em consideração apenas esses 3 caracteres de validação
    cont=0 # contador básico
    for i in range(0, 3):
        for j in range (0, tamanho -1):
            if caracteres[i] == email[j]:
                cont += 1
    if cont>=2 and cont<=3:
        return True
    else:
        return False 
        
    
def data_valida(data):
    # FlAVIUS ESSE CÓDIGO DE VALIDAÇÃO NÃO É NOSSO!
    # PEGAMOS NESTE LINK: https://pt.stackoverflow.com/questions/377579/validação-de-data-testes-com-python
    # faz o split e transforma em números
    dia, mes, ano = map(int, data.split('/'))

    # mês ou ano inválido (só considera do ano 1 em diante), retorna False
    if mes < 1 or mes > 12 or ano <= 0:
        return False

    # verifica qual o último dia do mês
    if mes in (1, 3, 5, 7, 8, 10, 12):
        ultimo_dia = 31
    elif mes == 2:
        # verifica se é ano bissexto
        if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
            ultimo_dia = 29
        else:
            ultimo_dia = 28
    else:
        ultimo_dia = 30

    # verifica se o dia é válido
    if dia < 1 or dia > ultimo_dia:
        return False

    return True


def validstring(nome): # Validação de strings
    palavras = 'ABCDEFG HIJKLMNOPQRSTUVXWYZÇ@!?*%$#&.,'
    nome = nome.upper()
    count = 0
    for i in range(len(palavras)):
        for j in range(len(nome)):
            if nome[j] == palavras[i]:
                count+=1
            
    if count == len(nome):
        return True
    else:
        return False


def validnum(num): # Validação de números, para usar no programa principal
    numeros = '0123456789'
    num = num.upper()
    count = 0
    for i in range(len(numeros)):
        for j in range(len(num)):
            if num[j] == numeros[i]:
                count+=1
            
    if count == len(num):
        return True
    else:
        return False

           
                
    