import sys
from datetime import datetime
from datetime import date
from colorama import init, AnsiToWin32



def clean_window():
    init(wrap=False)
    AnsiToWin32(sys.stderr).write("\x1b[2J\x1b[H")


def screen_costumer_initial():
    clean_window()
    print('''   
    | ==================================================================== |
    |                     Welcome to User Registration                     |
    | -------------------------------------------------------------------- |
    |                                                                      |
    |                Register new users                 [1]                |
    |                Change user data                   [2]                |
    |                Back to main menu                  [0]                |
    |                                                                      |
    | ==================================================================== |
    ''')

def screen_costumer_register_client():
     clean_window()
     print(''' 
          | ================================================== |
          |                     Neo Bank                       |
          |                                                    |
          |                Welcome to Register                |
          |       Come be our Neo client, let's register!      |
          |                                                    |
          | ------------------ since 2022 -------------------- |
     ''')

def screen_costumer_editing_client():
    clean_window()
    print(''' 
          | ================================================== |
          |                     Neo Bank                       |
          |                                                    |
          |                Welcome to Editing                 |
          |       Come be our Neo client, let's Editing        |
          |                                                    |
          | ------------------ since 2022 -------------------- |
     ''')
    
def screen_costumer_extract_client():
    clean_window()
    print(''' 
          | ================================================== |
          |                     Neo Bank                       |
          |                                                    |
          |                Wellcome to Extrato                 |
          |       Come be our Neo client, let's Extrato        |
          |                                                    |
          | ------------------ since 2022 -------------------- |
     ''')
 
def screen_costumer_delete_client():
    clean_window()
    print(''' 
    | -------------------  Vamos deletar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá deletar os seus dados! -------- |
    | ===================================================================================== |
            ''')

def screen_withdraw_main():
     
     clean_window()
     print('''     
     |----------------------------------------------------|
     |               Welcome to Financial                 |
     | ================================================== |
     |                                                    |
     |                                                    |                
     |               Deposit [1]                          |
     |               Withdrawal [2]                       |
     |               Transfers [3]                        |
     |               Benefits [4]                         |
     |               View balance [5]                     |
     |               Statement [6]                        |
     |               Back to main menu [0]                |
     |                                                    |
     | ================================================== |
       
     ''')

def screen_withdraw_deposit():
    clean_window()
    print('''
          | ------------------------------ Welcome to Deposit! ------------------------------------ |
          |          If you are registered in our system, you can make your deposit now!            |
          | ======================================================================================= |
      ''')
    
def screen_withdraw_subtration():
     clean_window()
     print('''
     | ----------------------------- Welcome to Withdrawal! ------------------------------ |
     |        If you are registered in our system, you can make your withdrawal now!       |
     | =================================================================================== |
     ''')

def screen_withdraw_balance():
    clean_window()
    print('''
          | ----------------------------- Welcome to Balance! --------------------------------- |
          |        If you are registered in our system, you can check your balance now!         |
          | =================================================================================== |
          ''')
def screen_withdraw_benefits():
        print(''' 
        |========================================================================================|
        |                          Welcome to the Awesome advantages!                            |
        |----------------------------------------------------------------------------------------|
        |              1 - We have the best annual rates for loans                               |
        |              2 - We have the best facilities for you to finance your home, your car,   |
        |                  or any type of property                                               |
        |              3 - We have the best credit lines for micro and small entrepeuners        |
        |              4 - Only here at Neo Bank, you can have a home broker completely perso    |
        |                  nalized for you who want to start your investiments!                  |
        |              5 - So what are you waiting for? Come join the AB family!                 |
        |========================================================================================|
        ''')

def screen_withdraw_statement():
     clean_window()
     print(''' 
    | ----------------------------- Welcome to your bank statement! -------------------------------- |
    |           If you are registered in our system, you can view your bank statement!               |
    | ============================================================================================== |
            ''')
       
def screen_withdraw_transfer():
        clean_window()
        print(f'''
        | =================== Transfers ===================== |
        |                                                     |
        |                                                     |
        |               1 - To AWB costumers                  |
        |               2 - To Non-costumers                  |
        |               3 - Back to main men                  |
        |                                                     |
        |                                                     |
        | ------------------ since 2023 --------------------- |
        | =================================================== |
              
        ''')
def screen_withdraw_transfer_option_one():
     clean_window()
     print(f'''

               Welcome to our transfer system, you have opted for the option 
               to transfer to a customer already registered in our system!
               
               We request the CPF of the registered person, so please have the 
               CPF in hand at the time of the transfer.    

          ''')