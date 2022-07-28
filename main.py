import cadastro
import saque
import deletar
import relatorio


#=========================== Simulador de Caixa Eletrônico ===============================#
def menu():
    while True:
        opcao = ' '
        print(''' =======================================
        ============== Banco Do Brasil =========================
        ========== Cadastro de cliente [1]  ====================
        ========== Saque em conta      [2]  ====================
        ========== Deletar conta       [3]  ====================
        ========== Sobre nós!          [4]
        ========== Sair do sistema     [5]  ====================
        =========================================================
        ''')
        opcao = input("Escolha a sua opção: ")

        if opcao == "1":
            cadastro()
        elif opcao == "2":
            saque()
        elif opcao == "3":
            deletar()
        elif opcao == "4":
            relatorio()
        




