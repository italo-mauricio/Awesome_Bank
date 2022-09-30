from cadaclientes import *
import os
from time import sleep




def emprest():
    while True:
        os.system("cls")
        hora_atual = datetime.now()
        hora = hora_atual.strftime('%H:%M')
        data = date.today()
        print(f'''
        ========================================================
                        data {data} / hora {hora}                   

                        1 - Solicitar Empréstimo
                        2 - Verificar as nossas taxas 
                        3 - Politicas da mpresa
                        4 - Voltar ao Menu Principal
                        
            
            
            
        =================== Since 2022 ========================
        
        ''')
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            pass
        elif opcao == '2':
            pass
        elif opcao == '3':
            pass
        elif opcao == '4':
            print("Saindo...")
            sleep(2)
            break
        else:
            print("Escolha uma opção válida")
            
            
            
            
