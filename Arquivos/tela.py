import PySimpleGUI as sg

class TelaBanco:
    def __init__(self):
        layout = [
            [sg.Text("Nome", size=(10,0)),sg.Input(size=(15,0), key='nome')],
            [sg.Text("Email", size=(10,0)),sg.Input(size=(15,0), key='email')],
            [sg.Text("Idade", size=(10,0)),sg.Input(size=(15,0), key='idade')],
            [sg.Text("Endereço", size=(10,0)),sg.Input(size=(15,0), key='endereco')],
            [sg.Text("Complemento", size=(10,0)),sg.Input(size=(15,0), key='complemento')],
            [sg.Text("Senha", size=(10,0)),sg.Input(size=(15,0), key='senha')],
            [sg.Button("Enviar Dados")]
        ]

        janela = sg.Window("Awesome Bank").layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values['nome']
        email = self.values['email']
        idade = self.values['idade']
        endereco = self.values['endereco']
        complemento = self.values['complemento']
        senha = self.values['senha']
        print(f'Nome: {nome}')
        print(f'Email: {email}')
        print(f'Idade: {idade}')
        print(f'Endereço: {endereco}')
        print(f'Complemento: {complemento}')
        print(f'Senha: {senha}')

