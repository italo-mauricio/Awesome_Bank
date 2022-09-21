import PySimpleGUI as sg






class Telabanco():
    def __init__(self):
        layout = [
            [sg.Text('CadastrarClientes'), sg.Input()],
            [sg.Text('SaqueemConta'), sg.Input()],
            [sg.Text('DeletarConta'), sg.Input()],
            [sg.Text('Consultarcotação'), sg.Input()],
            [sg.Button()]
            
            
        ]
        
        janela = sg.Window("Dados do usuário").layout(layout)
        self.button, self.values = janela.Read()
        
    def Iniciar(self):
        print(self.values)
        
tela = Telabanco()
tela.Iniciar()