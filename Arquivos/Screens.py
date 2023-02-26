import os

def clean_window():
    os.system("cls")


def screen_costumer_initial():
    clean_window
    print('''   
    | ==================================================================== |
    |                     Welcome to User Registration                     |
    | -------------------------------------------------------------------- |
    |                                                                      |
    |                Register new users                 [1]                |
    |                Bank Statement                     [2]                |
    |                Change user data                   [3]                |
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
 