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
            [sg.Slider(range=(0, 100), default_value=0, orientation='h', size=(15,20), key='slidervelocidade')],
            [sg.Button("Enviar Dados")],
            [sg.Output(size=(30,30))]
        ]

        self.janela = sg.Window("Awesome Bank").layout(layout)
        self.button, self.values = self.janela.Read()

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            email = self.values['email']
            idade = self.values['idade']
            endereco = self.values['endereco']
            complemento = self.values['complemento']
            senha = self.values['senha']
            velocidade_script = self.values['slidervelocidade']
            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Idade: {idade}')
            print(f'Endereço: {endereco}')
            print(f'Complemento: {complemento}')
            print(f'Senha: {senha}')
            print(f'Velocidade Script: {velocidade_script}')

