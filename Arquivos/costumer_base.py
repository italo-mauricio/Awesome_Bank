from screens import *
from validations import *
import pickle, os, pwinput
from time import sleep
from random import randint
from password import passw
from getpass import getpass
from datetime import datetime
from datetime import date
from archive import *
import os


def register_client():
    clean_window()
    while True:
        screen_costumer_initial()
        client = input("Choose your option: ")
        match client:
            case "1":
                create_account()
            case "2":
                edit_account()
            case "0":
                clean_window()
                break
            case _:
                print("Invalid Option!")
                input("Enter a valid option")
                os.system("cls")


# ------------------------------------------------------------------------------------- #


def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt).strip()
        if validation_func(user_input):
            return user_input
        else:
            print(f'Invalid {prompt.split(" ")[-1]}')


def create_account():
    current_time = datetime.now()
    hour = current_time.strftime("%H:%M")
    date_time = date.today()

    screen_costumer_register_client()

    name = get_valid_input("Type your Name: ", validstring)

    email = get_valid_input("Type your Email: ", validemail)

    address = input("Inform your address: ").strip()
    complement = input("Inform the complement (optional): ").strip()
    password = int(input("Type your password: "))
    balance = int(input("How much do you intend to deposit: "))

    id = gerandid.gera_id()
    print(f"Your registration ID is: {id}")

    while True:
        cpf = get_valid_input("Enter your CPF: ", cadastrocpf)
        if cpf not in dici:
            dici[password] = [name, email, address, complement, cpf, balance, id]
            print(
                f"""
                  Welcome {dici[password][0]} to the team! We are very happy to see you here!
                  | You were registered on the day {date_time} and at {hour} |
                  """
            )
            gravclientes(dici)
            break
        else:
            print("CPF already exists in the database")

    input("Press ENTER to continue...")
    clean_window()


# ------------------------------------------------------------------------------------------------------- #
def edit_account():
    screen_costumer_editing_client()

    while True:
        token = int(input("Insert your password: "))
        if token not in dici:
            print("User not found")
            break
        else:
            print("User found in the system")
            modify_user = (
                input("What data do you want to change in your registration: ")
                .strip()
                .lower()
            )

            if modify_user == "name":
                new_name = input("Please, type your new name: ").strip()
                if validstring(new_name):
                    dici[token][0] = new_name
                    print("Name changed successfully!")
                    gravclientes(dici)
                    break
                else:
                    print("Invalid Name")

            elif modify_user == "email":
                new_email = input("Please, type your new email: ").strip()
                if validemail(new_email):
                    dici[token][1] = new_email
                    print("Email changed successfully!")
                    gravclientes(dici)
                    break
                else:
                    print("Invalid Email!")

            elif modify_user == "address":
                new_address = input("Please, type your new address: ").strip()
                dici[token][2] = new_address
                print("New Address changed successfully!")
                gravclientes(dici)
                break

            elif modify_user == "optional":
                new_address_optional = input(
                    "Please, type your new (optional) address: "
                ).strip()
                dici[token][3] = new_address_optional
                print("New optional address changed successfully!")
                gravclientes(dici)
                break

            elif modify_user == "password":
                new_password = pwinput.pwinput(
                    "Please, type your new password: "
                ).strip()
                if validnum(new_password):
                    dici[token][5] = new_password
                    print("New Password changed successfully!")
                    gravclientes(dici)
                    break
                else:
                    print("Invalid Password")

            else:
                print("Invalid Option")


def delete_account():
    hora_atual = datetime.now()
    hora = hora_atual.strftime("%H:%M")
    data = date.today()  # Função para deletar usuário
    screen_costumer_delete_client()
    while True:
        print("Let's delete your user!")
        token = int(input("Please, type your password: "))

        if token not in dici:
            print("User not found!")
            break
        else:
            print("User Found!")
            del dici[token]
            print("User successfully deleted.")
            print(
                f"""
                Deletion Date: {data}
                Deletion Time: {hora_atual}
                    """
            )
            gravclientes(dici)
            input("Press ENTER for continue... ")
            break


class gerandid:  # gera uma ID para o cliente
    @staticmethod
    def gera_id():
        rand = randint(100000, 999999)
        return rand
